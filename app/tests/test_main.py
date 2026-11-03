import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.api import routes


client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_products():
    routes.products.clear()
    routes.next_product_id = 1
    yield
    routes.products.clear()
    routes.next_product_id = 1


def test_create_product():
    response = client.post(
        "/products/",
        json={
            "name": "Dell Laptop",
            "sku": "DELL-001",
            "quantity": 25,
            "price": 750.00
        }
    )

    assert response.status_code == 201
    assert response.json()["name"] == "Dell Laptop"
    assert response.json()["id"] == 1


def test_get_all_products():
    client.post(
        "/products/",
        json={
            "name": "Dell Laptop",
            "sku": "DELL-001",
            "quantity": 25,
            "price": 750.00
        }
    )

    response = client.get("/products/")


    assert response.status_code
    assert len(response.json()) == 1


def test_get_product_by_id():
    client.post(
        "/products/",
        json={
            "name": "Dell Laptop",
            "sku": "DELL-001",
            "quantity": 25,
            "price": 750.00
        }
    )

    response = client.get("/products/1")

    assert response.status_code == 200
    assert response.json()["sku"] == "DELL-001"


def test_update_product():
    client.post(
        "/products/",
        json={
            "name": "Dell Laptop",
            "sku": "DELL-001",
            "quantity": 25,
            "price": 750.00
        }
    )

    response = client.put(
        "/products/1",
        json={
            "name": "Dell Laptop Pro",
            "sku": "DELL-001",
            "quantity": 30,
            "price": 850.00
        }
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Dell Laptop Pro"
    assert response.json()["quantity"] == 30


def test_delete_product():
    client.post(
        "/products/",
        json={
            "name": "Dell Laptop",
            "sku": "DELL-001",
            "quantity": 25,
            "price": 750.00
        }
    )

    response = client.delete("/products/1")

    assert response.status_code == 204

    response = client.get("/products/1")

    assert response.status_code == 404


def test_duplicate_sku():
    product = {
        "name": "Dell Laptop",
        "sku": "DELL-001",
        "quantity": 25,
        "price": 750.00
    }

    client.post("/products/", json=product)
    response = client.post("/products/", json=product)

    assert response.status_code == 409


def test_product_not_found():
    response = client.get("/products/999")

    assert response.status_code == 404
