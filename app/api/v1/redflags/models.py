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

    def find_item(self, item_id):
        for item in db:
            if item["id"] == int(item_id):
                return item
        return None

    def update_red_flag(self, inc_id):
        data = {}
        data["id"] = int(inc_id)
        data["status"] = self.status
        data["createdOn"] = self.createdOn
        data["comment"] = self.comment
        data["location"] = self.location
        data["name"] = self.name

        flag = self.find_item(inc_id)

        if not flag:
            return {"Invalid incident Id"}, 400

        if flag['status'] != "new":
            return {"message": "Cannot be edited, incident is %s" % data["status"]}, 401

        flag.update(data)

        return db, 201

    def delete_incident(self, inc_id):
        flag = self.find_item(inc_id)
        if not flag:
            return "Invalid incident Id", 400
        db.remove(flag)
        return db
