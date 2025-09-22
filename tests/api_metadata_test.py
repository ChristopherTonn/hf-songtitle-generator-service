from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_metadata_endpoint_success():
    response = client.get("/metadata")
    assert response.status_code == 200
    json_data = response.json()
    
    # Check that we have both genres and moods
    assert "genres" in json_data
    assert "moods" in json_data
    
    # Check that genres and moods are lists
    assert isinstance(json_data["genres"], list)
    assert isinstance(json_data["moods"], list)
    
    # Check that we have some data
    assert len(json_data["genres"]) > 0
    assert len(json_data["moods"]) > 0
    
    # Check specific expected genres
    expected_genres = ["techno", "house", "trance", "ambient", "idm"]
    for genre in expected_genres:
        assert genre in json_data["genres"]
    
    # Check specific expected moods  
    expected_moods = ["dark", "happy", "relaxed", "uplifting"]
    for mood in expected_moods:
        assert mood in json_data["moods"]

def test_metadata_endpoint_sorted():
    response = client.get("/metadata")
    assert response.status_code == 200
    json_data = response.json()
    
    # Check that genres and moods are sorted
    assert json_data["genres"] == sorted(json_data["genres"])
    assert json_data["moods"] == sorted(json_data["moods"])