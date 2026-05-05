from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, auth
from ..database import get_db

router = APIRouter(prefix="/posts/{post_id}/comments", tags=["Comments"])

@router.get("/", response_model=List[schemas.CommentResponse])
def get_comments(post_id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post.comments

@router.post("/", status_code=201, response_model=schemas.CommentResponse)
def create_comment(
    post_id: int,
    comment: schemas.CommentCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    new_comment = models.Comment(
        content=comment.content,
        post_id=post_id,
        owner_id=current_user.id
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

@router.delete("/{comment_id}", status_code=204)
def delete_comment(
    post_id: int,
    comment_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    comment = db.query(models.Comment).filter(
        models.Comment.id == comment_id,
        models.Comment.post_id == post_id
    ).first()
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    if comment.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    db.delete(comment)
    db.commit()