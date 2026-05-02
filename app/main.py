from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import time
from . import models
from .database import engine
from .routers import posts, users, auth_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Blog API", version="0.4.0")

# ── CORS Middleware ───────────────────────────
# Allows frontend (React/Vue) to call your API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # In production: specify exact domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Custom Logging Middleware ─────────────────
# Logs every request: method, path, time taken
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start
    print(f"{request.method} {request.url.path} → {response.status_code} ({duration:.2f}s)")
    return response

# ── Global Exception Handler ──────────────────
# Catches any unhandled error and returns clean JSON
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error", "detail": str(exc)}
    )

# ── Routers ───────────────────────────────────
app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth_router.router)

@app.get("/")
def root():
    return {"message": "Blog API with Middleware!"}