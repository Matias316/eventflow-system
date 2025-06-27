def test_get_events_empty(http_client):
    response = http_client.get("/events/")
    assert response.status_code == 200
    assert response.json["events"] == []

def test_post_event(http_client):
    response = http_client.post("/events/", json={
        "title": "Test Event",
        "date": "2025-07-01"
    })
    assert response.status_code == 201
    assert "message" in response.json
