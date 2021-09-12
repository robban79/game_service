import json
import uuid
from flask_restful import Resource, reqparse
from the_chat import TheChat


class User:
    def __init__(self, name):
        self.name = name
        self.user_id = f'{uuid.uuid4()}'.replace("-", "")

    def to_string(self):
        return f'Name: {self.name}, id: {self.user_id}'


class UserApi(Resource):
    def __init__(self):
        self.user_args_parser = reqparse.RequestParser()
        self.user_args_parser.add_argument("name", type=str,
                                           help="Name of the person to create")

    @staticmethod
    def abort_if_name_exist(name):
        for user in TheChat.users:
            if user.name == name:
                return True
        return False

    def post(self):
        """
        post /user {name: "My name"}
        return: id
        """
        print("POST: ADD user")
        args = self.user_args_parser.parse_args()
        name = args["name"]
        if UserApi.abort_if_name_exist(name):
            return "{}", 422
        user = User(name)
        TheChat.users.append(user)
        return {"id": user.user_id}, 201

    def get(self):
        """
        get  /user
        return: id
        """
        print("GET: Get users")
        users = []
        for user in TheChat.users:
            users.append({"name": user.name})
        answer = {"users:": users}
        return json.dumps(answer), 200

    def put(self):
        print("PUT: Test printout users")
        for user in TheChat.users:
            print(user.to_string())
        return "", 200
