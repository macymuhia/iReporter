from time import strftime
from app.api.v1.redflags.models import Incident

db = []


class User:
    def __init__(self, name=None):
        self.id = len(db) + 1
        self.createdOn = strftime("%A, %B %d %Y %H:%M:%S")
        self.name = name
        self.db = db

    def create_user(self):
        data = {}
        data["id"] = self.id
        data["createdOn"] = self.createdOn
        data["name"] = self.name
        db.append(data)
        return data

    def get_all_users(self):
        return db

    def update_user(self, user_id):
        data = {}
        data["id"] = int(user_id)
        data["createdOn"] = self.createdOn
        data["name"] = self.name

        user = Incident().find_item(user_id)
        if not user:
            return "Id not found"
        user.update(data)

        return db

    def delete_user(self, user_id):
        user = Incident().find_item(user_id)
        if not user:
            return "Id not found"
        db.remove(user)
        return db
