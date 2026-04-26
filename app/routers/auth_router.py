from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import models, schemas, auth
from ..database import get_db

router = APIRouter(tags=["Authentication"])

@router.post("/login", response_model=schemas.Token)
def login(
    form: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = db.query(models.User).filter(
        models.User.email == form.username
    ).first()
    if not user or not auth.verify_password(form.password, user.password):
        raise HTTPException(status_code=403, detail="Invalid credentials")
    
    token = auth.create_access_token({"user_id": user.id})
    return {"access_token": token, "token_type": "bearer"}