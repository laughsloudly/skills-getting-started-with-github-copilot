def test_root_redirects_to_static_index(client):
    # Arrange

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code in (302, 307)
    assert response.headers["location"] == "/static/index.html"


def test_get_activities_returns_expected_structure(client):
    # Arrange

    # Act
    response = client.get("/activities")
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(data, dict)
    assert "Chess Club" in data

    chess = data["Chess Club"]
    assert "description" in chess
    assert "schedule" in chess
    assert "max_participants" in chess
    assert "participants" in chess
    assert isinstance(chess["participants"], list)
