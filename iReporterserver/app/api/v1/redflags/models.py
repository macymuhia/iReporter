from time import strftime

db = []

class Incident:

    def __init__(self, name=None, location=None, comment=None):
        self.id = len(db) + 1
        self.status = "new"
        self.createdOn = strftime("%A, %B %d %Y %H:%M:%S")
        self.comment = comment
        self.location = location
        self.name = name
        self.db = db

    def create_red_flag(self):
        data = {}
        data["id"] = self.id
        data["status"] = self.status
        data["createdOn"] = self.createdOn
        data["comment"] = self.comment
        data["location"] = self.location
        data["name"] = self.name
        db.append(data)
        return data

    def get_all_red_flags(self):
        return db

    def find_flag(self, inc_id):
        for flag in db:
            if flag['id'] == int(inc_id):
                return flag
        return None


    def update_red_flag(self, inc_id):
        data = {}
        data["id"] = inc_id
        data["status"] = self.status
        data["createdOn"] = self.createdOn
        data["comment"] = self.comment
        data["location"] = self.location
        data["name"] = self.name

        flag = self.find_flag(inc_id)
        if not flag:
            return "Id not found"
        flag.update(data)

        return db

    def delete_incident(self, inc_id):
        flag = self.find_flag(inc_id)
        if not flag:
            return "Id not found"
        db.remove(flag)
        return db
