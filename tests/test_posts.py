import pytest
from app import models

def test_get_all_posts(client):
    res = client.get("/posts/")
    assert res.status_code == 200
    assert isinstance(res.json(), list)

def test_create_post_unauthorized(client):
    res = client.post("/posts/", json={
        "title": "Test",
        "content": "Content",
        "published": True
    })
    assert res.status_code == 401

def test_create_post_authorized(authorized_client):
    res = authorized_client.post("/posts/", json={
        "title": "My First Post",
        "content": "Hello World",
        "published": True
    })
    assert res.status_code == 201
    assert res.json()["title"] == "My First Post"

def test_get_post_not_found(client):
    res = client.get("/posts/99999")
    assert res.status_code == 404

def test_delete_post_unauthorized(client, authorized_client):
    # Create a post first
    post = authorized_client.post("/posts/", json={
        "title": "Delete me",
        "content": "Content"
    }).json()
    # Try to delete without auth
    res = client.delete(f"/posts/{post['id']}")
    assert res.status_code == 401

def test_delete_post_authorized(authorized_client):
    post = authorized_client.post("/posts/", json={
        "title": "Delete me",
        "content": "Content"
    }).json()
    res = authorized_client.delete(f"/posts/{post['id']}")
    assert res.status_code == 204