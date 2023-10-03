import requests
import pytest
from unittest.mock import patch
from blog import Blog

posts = [
        {'userId': 1, 'id': 1, 'title': 'Titulo teste 1', 'body': 'Conteudo do blog 1'},
        {'userId': 2, 'id': 2, 'title': 'Titulo teste 2', 'body': 'Teste de conteudo do blog 2'}
]

@pytest.fixture
def fake_posts():
    return posts


def test_post(fake_posts):
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = fake_posts
        blog = Blog()
        result = blog.posts()
        mock_get.assert_called_once_with("https://jsonplaceholder.typicode.com/posts")
        assert result == fake_posts

@pytest.mark.parametrize("user_id, expected_post", [
    (1, posts[0]),
    (2, posts[1])
])
def test_post_by_user_id(fake_posts, user_id, expected_post):
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = expected_post
        blog = Blog()
        result = blog.post_by_user_id(user_id)
        expected_url = f"https://jsonplaceholder.typicode.com/posts/{user_id}"
        mock_get.assert_called_once_with(expected_url)
        assert result == result == expected_post

if __name__ == "__main__":
    pytest.main()