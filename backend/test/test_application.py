from unittest import TestCase
from fastapi.testclient import TestClient
from backend.application import application as app

client = TestClient(app)


class Test(TestCase):
    def test_root(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Welcome to MyMEAL api!"})

    def test_get_all_users(self):
        response = client.get("/users")
        self.assertEqual(response.status_code, 200)
        from backend.src.dto import user_dto
        self.assertIsInstance(response.json(), [user_dto.UserDto])
