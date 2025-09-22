from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_metadata():
    """Test metadata endpoint for frontend UI data."""
    response = client.get("/metadata/")
    assert response.status_code == 200
    data = response.json()
    
    # Check response structure
    assert "genres" in data
    assert "moods" in data
    assert isinstance(data["genres"], list)
    assert isinstance(data["moods"], list)
    
    # Should have data
    assert len(data["genres"]) > 0
    assert len(data["moods"]) > 0
    
    # Check that extended_mood_map is not in genres
    assert "extended_mood_map" not in data["genres"]
    
    # Check common entries exist
    assert "techno" in data["genres"]
    assert "ambient" in data["genres"]
    assert "idm" in data["genres"]
    
    # Check moods from extended_mood_map
    expected_moods = ["dark", "happy", "psychedelic", "relaxed", "uplifting"]
    for mood in expected_moods:
        assert mood in data["moods"]
    
    print(f"✅ Available genres: {data['genres']}")
    print(f"✅ Available moods: {data['moods']}")

def test_metadata_genres_sorted():
    """Test that genres are returned sorted."""
    response = client.get("/metadata/")
    assert response.status_code == 200
    data = response.json()
    
    genres = data["genres"]
    assert genres == sorted(genres), "Genres should be sorted alphabetically"

def test_metadata_moods_sorted():
    """Test that moods are returned sorted."""
    response = client.get("/metadata/")
    assert response.status_code == 200
    data = response.json()
    
    moods = data["moods"]
    assert moods == sorted(moods), "Moods should be sorted alphabetically"