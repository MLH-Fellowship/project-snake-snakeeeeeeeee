
import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):

        self.client = app.test_client()
    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>David & Enrique</title>" in html
        assert "<a href=" in html
        assert "<footer" in html

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        get_json = response.get_json()
        assert "timeline_posts" in get_json
        assert len(get_json["timeline_posts"]) == 0
        
        post = self.client.post("/api/timeline_post", data={'name': 'Test', 'email': 'test@poo.com', 'content': 'fewweesdd'})
        assert post.status_code == 200
        assert post.is_json
        response = self.client.get("api/timeline_post")
        post_json = response.get_json()
        assert"timeline_posts" in post_json
        assert len(post_json["timeline_posts"]) != 0

        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert '<form action="/api/timeline_post" method="post"' in html
        assert 'id="name"' in html
        assert 'id="email"' in html
        assert 'id="content"' in html

    def test_malformed_timeline_post(self):

            response = self.client.post("/api/timeline_post", data={"email": "john@example.com", "content": "Hello world, I'm John!"})
            assert response.status_code == 400
            html = response.get_data(as_text=True)
            assert "Invalid name" in html

            response = self.client.post("api/timeline_post", data={"name": "John Doe", "email": "john@example.com", "content": ""})
            assert response.status_code == 400
            html = response.get_data(as_text=True)
            assert "Invalid content" in html

            response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "non-an-email", "content": "Hello"})
            assert response.status_code == 400
            html = response.get_data(as_text=True)
            assert "Invalid emial" in html

