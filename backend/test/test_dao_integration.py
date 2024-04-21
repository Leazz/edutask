# test_dao_integration.py
import pytest
from src.util.dao import DAO

@pytest.fixture(scope="module")
def user_dao(mongo_db):
    return DAO('users')  # Pass only the collection name

@pytest.fixture(scope="module")
def task_dao(mongo_db):
    return DAO('tasks')  # Pass only the collection name

def test_create_user(user_dao):
    user_data = {"name": "John Doe", "email": "john@example.com"}
    result = user_dao.create(user_data)
    assert result['inserted_id'] is not None
    assert result['acknowledged']

def test_create_task(task_dao):
    task_data = {"title": "Finish report", "description": "Complete the annual report by Friday"}
    result = task_dao.create(task_data)
    assert result['inserted_id'] is not None
    assert result['acknowledged']

def test_valid_input(user_dao):
    # Assume the dao.create() returns some identifier or success message
    result = user_dao.create({'name': 'John Doe', 'email': 'john@example.com'})
    assert result is not None

def test_invalid_input(user_dao):
    # Assume dao.create() raises an exception or returns None for invalid data
    with pytest.raises(ValueError):
        user_dao.create({'name': '', 'email': 'invalid-email'})

def test_database_connection(user_dao):
    # You could simulate a database connection issue here
    # This might involve mocking MongoClient to throw a ConnectionFailure exception
    with pytest.raises(ConnectionError):
        user_dao.create({'name': 'Test User', 'email': 'test@example.com'})

def test_data_integrity(user_dao):
    user_data = {'name': 'Jane Doe', 'email': 'jane@example.com'}
    user_id = user_dao.create(user_data)
    assert user_dao.findOne(user_id) == user_data
