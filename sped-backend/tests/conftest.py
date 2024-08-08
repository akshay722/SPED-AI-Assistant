import pytest
from pymongo import MongoClient
from pymongo.uri_parser import parse_uri
import subprocess
import time
from dotenv import load_dotenv
import os

load_dotenv()


@pytest.fixture(scope="session", autouse=True)
def drop_collections_before_and_after_tests():
    MONGODB_URL = os.environ.get("DATABASE_URL")

    client = MongoClient(MONGODB_URL)
    customer_db_name = parse_uri(MONGODB_URL)["database"]
    db = client[customer_db_name]

    # List of collection names to drop before running tests
    collections_to_drop = db.list_collection_names()

    # Get a list of all collection names in the database
    print("Dropping collections before tests:", collections_to_drop)
    for collection_name in collections_to_drop:
        db[collection_name].drop()

    yield

    # Code here will run after all tests have completed

    # List of collection names to drop after running tests
    collections_to_drop = db.list_collection_names()

    # Get a list of all collection names in the database
    print("Dropping collections after tests:", collections_to_drop)
    for collection_name in collections_to_drop:
        db[collection_name].drop()

    # Clean up resources (optional)
    client.close()


@pytest.fixture(scope="session", autouse=True)
def server():
    # Start the server
    # subprocess.Popen(["sudo", "./services.sh", "start"])
    # drop_collections_before_tests()
    local = subprocess.Popen(["python3", "app.py"])

    time.sleep(5)  # Allow time for the server to start
    yield

    # Code here will run after all tests have completed

    # Stop the server
    # subprocess.run(["sudo", "./services.sh", "stop"])
    local.terminate()
