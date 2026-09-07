def test_predict_returns_average(client):
    response = client.post("/api/v1/predict", json={"features": [2.0, 4.0]})

    assert response.status_code == 200
    assert response.json() == {"prediction": 3.0}


def test_predict_with_no_features_returns_zero(client):
    response = client.post("/api/v1/predict", json={"features": []})

    assert response.status_code == 200
    assert response.json() == {"prediction": 0.0}
