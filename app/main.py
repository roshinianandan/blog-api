from fastapi import FastAPI
from . import models
from .database import engine
from .routers import posts, users, auth_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Blog API", version="0.3.0")

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth_router.router)

@app.get("/")
def root():
    return {"message": "Blog API with JWT Auth!"}