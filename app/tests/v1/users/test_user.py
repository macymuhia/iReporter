import unittest
from ..base_test import BaseTestCase
import json


class UserTestCase(BaseTestCase):
    def test_api_gets_all_users(self):
        response = self.client.get("api/v1/users")
        self.assertEqual(response.status_code, 200)

    def test_redflag_can_be_created(self):
        res = self.client.post(
            "api/v1/users", data=json.dumps(self.user), content_type="application/json"
        )
        self.assertEqual(res.status_code, 201)

    def test_api_can_get_user_by_id(self):
        """ create a new user """
        response = self.client.post(
            "api/v1/users", data=json.dumps(self.user), content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)
        result_in_json = json.loads(response.data.decode("utf-8").replace("'", '"'))

        """ get the new red user by id """
        result = self.client.get("api/v1/users/{}".format(result_in_json["id"]))
        self.assertEqual(result.status_code, 200)

    def test_user_can_be_edited(self):
        """ create a new user """
        ps_res = self.client.post(
            "api/v1/users", data=json.dumps(self.user), content_type="application/json"
        )
        self.assertEqual(ps_res.status_code, 201)

        """ get the new user by id """
        user_update = {"name": "Aviana", "location": "122,3344", "comment": "rejected"}
        pt_res = self.client.put(
            "api/v1/users/1",
            data=json.dumps(user_update),
            content_type="application/json",
        )
        self.assertEqual(pt_res.status_code, 201)

    def test_user_can_be_deleted(self):
        post_res = self.client.post("api/v1/users", data=json.dumps(self.user), content_type="application/json")
        self.assertEqual(post_res.status_code, 201)
        delete_res = self.client.delete("api/v1/users/1")
        self.assertEqual(delete_res.status_code, 200)


if __name__ == "__main__":
    unittest.main()
