from flask import request
from flask_restful import Resource
from .models import db, Incident


class RedFlagList(Resource):
    def get(self):
        return Incident().get_all_red_flags(), 200

    def post(self):
        data = request.get_json()
        name = data["name"]
        location = data["location"]
        comment = data["comment"]
        instance = Incident(name, location, comment)
        return instance.create_red_flag(), 201


class RedFlag(Resource):
    def get(self, red_flag_id):
        found_flag = {}
        for flag in db:
            if flag["id"] == int(red_flag_id):
                found_flag = flag
                break
        return found_flag, 200

    def put(self, red_flag_id):
        data = request.get_json()

        if not red_flag_id:
            return {"message": "Please provide incident id"}, 400

        name = data["name"]
        location = data["location"]
        comment = data["comment"]

        inc = Incident(name, location, comment)
        return inc.update_red_flag(red_flag_id), 201

    def delete(self, red_flag_id):
        if not red_flag_id:
            return {"message": "Please provide incident id"}, 400

        return Incident().delete_incident(red_flag_id)
