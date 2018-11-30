import unittest
from app import create_app
from app.api.v1 import blueprint


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")

        self.app.register_blueprint(blueprint)

        self.client = self.app.test_client()

        self.red_flag = { "comment": "rejected", "location": "122,3344", "name": "macy" }
        self.user = { "name": "macy" }