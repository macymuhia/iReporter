from flask import request
from flask_restful import Resource
from app.api.v1.users.models import db, User


class UserList(Resource):
    def get(self):
        return User().get_all_users(), 200

    def post(self):
        data = request.get_json()
        name = data["name"]
        instance = User(name)
        return instance.create_user(), 201


class SingleUser(Resource):
    def get(self, user_id):
        found_user = {}
        for user in db:
            if user["id"] == int(user_id):
                found_user = user
                break
        return found_user, 200

    def put(self, user_id):
        data = request.get_json()

        if not user_id:
            return {"message": "Please provide user id"}, 400

        name = data["name"]

        instance = User(name)
        return instance.update_user(user_id), 201

    def delete(self, user_id):
        if not user_id:
            return {"message": "Please provide user id"}, 400

        return User().delete_user(user_id)
