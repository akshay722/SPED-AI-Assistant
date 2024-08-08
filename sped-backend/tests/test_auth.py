import requests
from dotenv import load_dotenv
import os

load_dotenv()
TEST_LOCAL_URL = os.environ.get("TEST_LOCAL_URL")


# -------------------------------------------- Signup -------------------------------------------- #
def test_create_user_success():
    # Create a sample signup request
    signup_request = {
        "userName": "test_user",
        "email": "test@example.com",
        "password": "Test@123",
        "cPassword": "Test@123",
    }

    # Send the signup request
    response = requests.post(f"{TEST_LOCAL_URL}v1/signup", json=signup_request)
    # Assert the response status code
    assert response.status_code == 201

    # Assert the response data
    data = response.json()
    assert "_id" in data


def test_create_user_already_exists():
    # Create a signup request for an existing user
    signup_request = {
        "userName": "test user",
        "email": "test@example.com",
        "password": "Test@123",
        "cPassword": "Test@123",
    }

    # Send the signup request
    response = requests.post(f"{TEST_LOCAL_URL}v1/signup", json=signup_request)

    # Assert the response status code
    assert response.status_code == 400

    # Assert the response detail
    assert response.json() == {"error": "User with this email already exist"}


# -------------------------------------------- Login -------------------------------------------- #
def test_login_success():
    # Create a sample login request
    login_request = {"email": "test@example.com", "password": "Test@123"}

    # Send the login request
    response = requests.post(f"{TEST_LOCAL_URL}v1/login", json=login_request)

    # Assert the response status code
    assert response.status_code == 200

    # Assert the response data
    data = response.json()
    assert "access_token" in data
    assert "user" in data
    assert "refresh_token" in data


def test_login_user_not_found():
    # Create a login request for a non-existent user
    login_request = {
        "email": "test1234@example.com",
        "password": "Test@123",
    }

    # Send the login request
    response = requests.post(f"{TEST_LOCAL_URL}v1/login", json=login_request)

    # Assert the response status code
    assert response.status_code == 404

    # Assert the response detail
    data = response.json()
    assert "error" in data
    assert data["error"] == "User is not Found"


def test_login_incorrect_password():
    # Create a login request with incorrect password
    login_request = {"email": "test@example.com", "password": "Test@1234566"}

    # Send the login request
    response = requests.post(f"{TEST_LOCAL_URL}v1/login", json=login_request)

    # Assert the response status code
    assert response.status_code == 422

    # Assert the response detail
    data = response.json()
    assert "error" in data
    assert data["error"] == "Incorrect password"
