from core.user.models import User

def test_create_user():
    user =User(username='testuser', email='testemail@gmail.com', hashed_password="password")
    assert user.username == 'testuser'
    assert user.email == 'testemail@gmail.com'
    assert user.hashed_password == "password"