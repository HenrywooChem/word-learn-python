import requests
import json

# Test registration with detailed error
data = {
    "name": "testuser",
    "username": "testuser456",
    "password": "test123",
    "role": "parent"
}

try:
    response = requests.post("http://localhost:8000/api/auth/register", json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    if response.status_code >= 400:
        print(f"Headers: {response.headers}")
except Exception as e:
    print(f"Error: {e}")
