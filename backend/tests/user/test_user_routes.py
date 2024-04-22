from fastapi.testclient import TestClient
from app import app
from faker import Faker

fake = Faker()
client = TestClient(app)


def get_user_data():
    user_data = {
        'username': fake.name(),
        'email': fake.email(),
        'password': 'password1',
    }

    client.post('/user/signup', json=user_data)

    return user_data


def test_signup():
    signup_data = {
        'username': fake.name(),
        'email': fake.email(),
        'password': 'password1'
    }
    response = client.post('/user/signup', json=signup_data)
    assert response.status_code == 200
    assert response.json() == {
        'message':  'User has been created'
    }


def test_login():
    test_login_data = get_user_data()
    response = client.post('/user/login', json=test_login_data)
    
    assert response.status_code == 200
    assert 'access_token' in response.json()
    assert response.json()['token_type'] == 'bearer'
