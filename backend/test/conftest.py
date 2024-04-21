import pytest
from pymongo import MongoClient
from src.util.dao import DAO

@pytest.fixture(scope='module')
def mongo_db():
    client = MongoClient('mongodb://localhost:27017/')
    db = client.test_database
    yield db
    client.drop_database('test_database')  # Clean up after tests

@pytest.fixture(scope='module')
def user_dao():
    return DAO('users')

@pytest.fixture(scope='module')
def task_dao():
    # Create an instance of DAO specifically for task operations
    return DAO('tasks')
