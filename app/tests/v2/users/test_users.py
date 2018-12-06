import unittest
from app.tests.v2.base_test import BaseTestCase
import json


class UserTestCase(BaseTestCase):
   def test_user_login_with_valid_password(self):
       response = self.client.post(
           "api/v2/signin",
           data=json.dumps(self.login_user),
           content_type="application/json",
       )
       self.assertEqual(response.status_code, 200)

   def test_user_login_with_invalid_password(self):
       response = self.client.post(
           "api/v2/signin",
           data=json.dumps(self.invalid_login_user),
           content_type="application/json",
       )
       json_data = json.loads(response.data)
       self.assertEqual(response.status_code, 400)
       self.assertTrue(json_data.get("error"))

   def test_user_login_with_invalid_email(self):
       response = self.client.post(
           "api/v2/signin",
           data=json.dumps(self.invalid_login_email),
           content_type="application/json",
       )
       json_data = json.loads(response.data)
       self.assertEqual(response.status_code, 400)
       self.assertTrue(json_data.get("error"))

    def test_user_signup(self):
       response = self.client.post(
           "api/v2/signup",
           data=json.dumps(self.create_user),
           content_type="application/json",
       )
       json_data = json.loads(response.data)
       self.assertEqual(response.status_code, 200)
       resp_data = json_data.get("data")
       self.assertEqual(resp_data[0]["message"], "Created Successfully")

   def test_password_confirm_password_match(self):
       response = self.client.post(
           "api/v2/signup",
           data=json.dumps(self.create_user),
           content_type="application/json",
       )
       json_data = json.loads(response.data)
       self.assertEqual(response.status_code, 400)

   def test_edit_user(self):
       auth_token = self.auth()
       response = self.client.put(
           'api/v2/users/{userId}',
           data=json.dumps(self.edit_user),
           headers={'Authorization': 'Bearer %s' % auth_token, 'content_type': 'application/json'}
       ).format(userId=1)

       self.assertEqual(response.status_code, 201)

    def test_delete_user(self):
       auth_token = self.auth()
       response = self.client.delete(
           'api/v2/users/{userId}',
           headers={'Authorization': 'Bearer %s' % auth_token, 'content_type': 'application/json'}
       ).format(userId=1)

       self.assertEqual(response.status_code, 204)

   def test_get_user_by_id(self):
       auth_token = self.auth()
       response = self.client.get(
           'api/v2/users/{userId}',
           headers={'Authorization': 'Bearer %s' % auth_token, 'content_type': 'application/json'}
       ).format(userId=1)

       self.assertEqual(response.status_code, 200)

   def test_get_all_user(self):
       auth_token = self.auth()
       response = self.client.get(
           'api/v2/users',
           headers={'Authorization': 'Bearer %s' % auth_token, 'content_type': 'application/json'}
       )
       self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
   unittest.main()
