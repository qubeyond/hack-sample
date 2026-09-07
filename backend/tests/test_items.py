def test_create_and_list_items(client):
    created = client.post("/api/v1/items", json={"name": "test item"})
    assert created.status_code == 200
    assert created.json()["name"] == "test item"

    items = client.get("/api/v1/items")
    assert items.status_code == 200
    assert any(item["name"] == "test item" for item in items.json())


def test_get_missing_item_returns_404(client):
    response = client.get("/api/v1/items/999999")

    assert response.status_code == 404
