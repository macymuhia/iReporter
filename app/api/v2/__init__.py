from flask import Blueprint
from flask_restful import Api
from app.api.v1.redflags.views import RedFlagList, RedFlag
from app.api.v1.users.views import UserList, SingleUser

blueprint_v2 = Blueprint("api_v2", __name__)
api = Api(blueprint_v2, prefix="/api/v2")