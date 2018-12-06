import unittest
from app import create_app
import json


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.create_user = {
            "email": "john.doe@example.com",
            "name": "John Doe",
            "password": "pass"
        }

        self.edit_user = {
            "email": "jane.doe@example.com",
            "name": "Jane Doe"
        }

        self.login_user = {
            "email": "john.doe@example.com",
            "password": "pass"
        }

        self.invalid_login_user = {
            "email": "john.doe@example.com"
        }

        self.invalid_login_email = {
            "email": "invalidexample.com"
        }

    def auth(self):
        response = self.client.post(
            "api/v2/signin",
            data=json.dumps(self.login_user),
            content_type="application/json",
        )
        data = json.loads(response.data.decode())
        auth_token = data['token']
        self.assertTrue(auth_token)
        return auth_token

    def tearDown(self):
        pass
