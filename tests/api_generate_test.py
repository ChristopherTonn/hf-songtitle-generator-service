from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_generate_endpoint_success():
    response = client.post("/generate", json={
        "genre": "techno",
        "mood": "dark",
        "custom_words": ["Neuro", "Dronewave"]
    })
    assert response.status_code == 200
    json_data = response.json()
    assert "title" in json_data
    assert isinstance(json_data["title"], str)
    assert len(json_data["title"]) > 0
