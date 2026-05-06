# Blog API 🚀

A production-ready REST API built with **FastAPI**, **PostgreSQL**, and **JWT Authentication**.

## Tech Stack
- **FastAPI** — Python web framework
- **PostgreSQL** — Relational database
- **SQLAlchemy** — ORM for database operations
- **JWT** — Secure authentication with python-jose
- **bcrypt** — Password hashing with passlib
- **Pydantic** — Data validation
- **Uvicorn** — ASGI server

## Features
- ✅ User registration and login
- ✅ JWT token authentication
- ✅ Full CRUD for blog posts
- ✅ Owner-based permissions (only creator can edit/delete)
- ✅ Search and pagination
- ✅ CORS middleware
- ✅ Global error handling
- ✅ Request logging middleware

## Project Structure

## Docker Setup

### Run with Docker Compose
```bash
docker-compose up --build
```

### Stop containers
```bash
docker-compose down
```

## CI/CD
This project uses **GitHub Actions** for continuous integration.
- Every push to `main` runs the full pytest suite automatically
- Badge: ![CI](https://github.com/roshinianandan/blog-api/actions/workflows/ci.yml/badge.svg)

## Deployment
Deployed on **Render.com** — [Live API URL here]

### Deploy your own
1. Fork this repo
2. Connect to Render.com
3. Set environment variables
4. Deploy!