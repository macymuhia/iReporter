from flask import Blueprint
from flask_restful import Api
from app.api.v1.redflags.views import RedFlagList, RedFlag
from app.api.v1.users.views import UserList, SingleUser

blueprint = Blueprint("api_v1", __name__)
api = Api(blueprint, prefix="/api/v1")

api.add_resource(RedFlagList, "/redflags")
api.add_resource(RedFlag, "/redflags/<red_flag_id>")

api.add_resource(UserList, "/users")
api.add_resource(SingleUser, "/users/<user_id>")
