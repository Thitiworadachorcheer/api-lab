import uuid


# A second user with a name that is already taken gets 400.
def test_duplicate_username_is_refused(api):
    name = "lab-" + uuid.uuid4().hex[:12]
    user = {"username": name, "password": "Pizza-2026"}
    res1 = api.post("/api/users", json=user)
    assert res1.status_code == 201
    res2 = api.post("/api/users", json=user)
    assert res2.status_code == 400
    assert res2.json() == {"error": "username already taken"}


# Logging in with a wrong password gets 401.
def test_wrong_password_is_refused(api):
    name = "lab-" + uuid.uuid4().hex[:12]
    user = {"username": name, "password": "Pizza-2026"}
    res = api.post("/api/users", json=user)
    assert res.status_code == 201
    bad_login = {"username": name, "password": "WrongPassword"}
    res_login = api.post("/api/users/token/login", json=bad_login)
    assert res_login.status_code == 401
    assert res_login.json() == {"error": "authentication failed"}


# A user with an empty name gets 400.
def test_empty_username_is_refused(api):
    user = {"username": "", "password": "Pizza-2026"}
    res = api.post("/api/users", json=user)
    assert res.status_code == 400
    assert res.json() == {"error": "username field is empty"}