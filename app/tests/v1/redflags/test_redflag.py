import unittest
from ..base_test import BaseTestCase
import json


class RedFlagTestCase(BaseTestCase):
    def test_api_gets_all_redflags(self):
        response = self.client.get("api/v1/redflags")
        self.assertEqual(response.status_code, 200)

    def test_redflag_can_be_created(self):
        res = self.client.post(
            "api/v1/redflags",
            data=json.dumps(self.red_flag),
            content_type="application/json",
        )
        self.assertEqual(res.status_code, 201)

    def test_api_can_get_redflag_by_id(self):
        """ create a new red flag """
        response = self.client.post(
            "api/v1/redflags",
            data=json.dumps(self.red_flag),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        result_in_json = json.loads(response.data.decode("utf-8").replace("'", '"'))
        """ get the new red flag by id """
        result = self.client.get("api/v1/redflags/{}".format(result_in_json["id"]))
        self.assertEqual(result.status_code, 200)

    def test_redflag_can_be_edited(self):
        """ create a new red flag """
        ps_res = self.client.post(
            "api/v1/redflags",
            data=json.dumps(self.red_flag),
            content_type="application/json",
        )
        self.assertEqual(ps_res.status_code, 201)

        """ get the new red flag by id """
        red_flag_update = {
            "name": "Aviana",
            "location": "122,3344",
            "comment": "rejected",
        }
        pt_res = self.client.put(
            "api/v1/redflags/1",
            data=json.dumps(red_flag_update),
            content_type="application/json",
        )
        self.assertEqual(pt_res.status_code, 201)


if __name__ == "__main__":
    unittest.main()
