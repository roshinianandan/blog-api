def test_register_user(client):
    res = client.post("/users/", json={
        "email": "newuser@test.com",
        "password": "password123"
    })
    assert res.status_code == 201
    assert res.json()["email"] == "newuser@test.com"
    assert "id" in res.json()
    assert "password" not in res.json()  # password never returned!

def test_register_duplicate_email(client, test_user):
    res = client.post("/users/", json={
        "email": "test@test.com",
        "password": "password123"
    })
    assert res.status_code == 400

def test_login_success(client, test_user):
    res = client.post("/login", data={
        "username": test_user["email"],
        "password": "password123"
    })
    assert res.status_code == 200
    assert "access_token" in res.json()
    assert res.json()["token_type"] == "bearer"

def test_login_wrong_password(client, test_user):
    res = client.post("/login", data={
        "username": test_user["email"],
        "password": "wrongpassword"
    })
    assert res.status_code == 403

def test_login_wrong_email(client):
    res = client.post("/login", data={
        "username": "nobody@test.com",
        "password": "password123"
    })
    assert res.status_code == 403