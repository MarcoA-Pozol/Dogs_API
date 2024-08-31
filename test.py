from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)

def test_create_breed():
    new_breed = {
            "name": "TestBreed2",
            "breed_origin": "Siberia",
            "weight": 20.0,
            "height": 55.0,
            "ear_type": "Erect",
            "energy_level": "High",
            "life_expectancy": 12,
            "drooling_tendency": "Low",
            "snoring_tendency": "Low",
            "barking_tendency": "Moderate",
            "digging_tendency": "Moderate",
            "attention_need": "High",
            "breed_for": "Sled pulling",
            "coat_length": "Medium",
            "coat_type": "Double coat",
            "coat_colors": "Black and White, Red and White, etc.",
            "grooming_need": "Moderate",
        }
    
    response = client.post(
        "/breeds/",
        json=new_breed
    )
    
    # Check that the response status code is 201 (Created)
    assert response.status_code == 201 or response.status_code == 200
    
    # Check that the breed name in the response matches the input
    assert response.json()["name"] == new_breed["name"]
    assert response.json()["breed_origin"] == new_breed["breed_origin"]
    assert response.json()["weight"] == new_breed["weight"]

# Test for getting all breeds
def test_get_breeds():
    response = client.get("/breeds/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    
def test_get_breed():
    response = client.get("/breeds/21")
    assert response.status_code == 200
    assert response.json()["id"] == 21
    assert response.json()["name"] == "Siberian Husky"  # Ensure this matches the created breed name

# Test for creating a new dog
def test_create_dog():
    new_dog = {
        "name": "TestDog1",
        "age": 2,
        "weight": 35.0,
        "height": 65.0,
        "coat_colors": "White and Gray",
        "breed_id": 24
    }
    response = client.post("/dogs/", json=new_dog)
    assert response.status_code == 201 or response.status_code == 200
    assert response.json()["name"] == new_dog["name"]

# Test for getting all dogs
def test_get_dogs():
    response = client.get("/dogs/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test for getting a specific dog by ID
def test_get_dog():
    response = client.get("/dogs/10")
    assert response.status_code == 200
    assert response.json()["id"] == 10
    assert response.json()["name"] == "TestDog1"

# Test for updating a dog
def test_update_dog():
    updated_dog = {
        "name": "Pablo",
        "age": 4,
        "weight": 26.0,
        "height": 51.0,
        "coat_colors": "Black and Tan",
        "breed_id": 5
    }
    response = client.put("/dogs/12", json=updated_dog)
    assert response.status_code == 200 or response.status_code == 404 # 404 in the case the response did not match any instance or it does not already exist

# Test for deleting a dog
def test_delete_dog():
    response = client.delete("/dogs/11")
    assert response.status_code == 200 or response.status_code == 404 # 404 in the case the response did not match any instance or it does not already exist
