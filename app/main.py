from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import time
from .routers import posts, users, auth_router, comments

app = FastAPI(title="Blog API", version="0.6.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start
    print(f"{request.method} {request.url.path} → {response.status_code} ({duration:.2f}s)")
    return response

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error", "detail": str(exc)}
    )

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth_router.router)
app.include_router(comments.router)

@app.get("/")
def root():
    return {"message": "Blog API v0.6.0"}