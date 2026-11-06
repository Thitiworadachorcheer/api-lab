import pytest


# Boundary values for PUT /api/ratings/{id}: 1 and 5 pass, 0 and 6 fail.
@pytest.mark.parametrize(
    "stars, expected_status",
    [
        (0, 400),
        (1, 200),
        (5, 200),
        (6, 400),
    ],
)
def test_update_rating_boundary_values(
    api, auth, rating, stars, expected_status
):
    path = f"/api/ratings/{rating['id']}"
    initial_stars = rating["stars"]
    res = api.put(path, json={"stars": stars}, headers=auth)
    assert res.status_code == expected_status

    check_res = api.get(path, headers=auth)
    assert check_res.status_code == 200
    if expected_status == 200:
        assert check_res.json()["stars"] == stars
    else:
        assert check_res.json()["stars"] == initial_stars