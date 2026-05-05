from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__ = "users"

    id         = Column(Integer, primary_key=True, index=True)
    email      = Column(String, unique=True, nullable=False)
    password   = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

    posts      = relationship("Post", back_populates="owner",
                              cascade="all, delete-orphan")

class Post(Base):
    __tablename__ = "posts"

    id         = Column(Integer, primary_key=True, index=True)
    title      = Column(String, nullable=False)
    content    = Column(String, nullable=False)
    published  = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    owner_id   = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"),
                        nullable=False)
    owner      = relationship("User", back_populates="posts")

class Comment(Base):
    __tablename__ = "comments"

    id         = Column(Integer, primary_key=True, index=True)
    content    = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    post_id    = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"),
                        nullable=False)
    owner_id   = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"),
                        nullable=False)
    post       = relationship("Post", backref="comments")
    owner      = relationship("User", backref="comments")