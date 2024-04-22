from core.post.models import Post
from core.users.models import User

def test_create_post():
    post =Post(title='testtitle', content='testcontent')
    assert post.title == 'testtitle'
    assert post.content == 'testcontent'

def test_user_post_relationship():
    user =User(username='testuser', email='testemail@gmail.com', hashed_password="password")
    post =Post(title='testtitle', content='testcontent', author=user)
    assert post.author == user