from time import strftime

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

    def find_user(self, user_id):
        for flag in db:
            if flag["id"] == int(user_id):
                return flag
        return None

    def update_user(self, user_id):
        data = {}
        data["id"] = user_id
        data["createdOn"] = self.createdOn
        data["name"] = self.name

        user = self.find_user(user_id)
        if not user:
            return "Id not found"
        user.update(data)

        return db

    def delete_user(self, user_id):
        user = self.find_user(user_id)
        if not user:
            return "Id not found"
        db.remove(user)
        return db
