from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# ── Post Schemas ──────────────────────────────
class PostCreate(BaseModel):
    title: str
    content: str
    published: bool = True

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    created_at: datetime

    class Config:
        from_attributes = True

# ── User Schemas ──────────────────────────────
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True

# ── Token Schemas ─────────────────────────────
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None