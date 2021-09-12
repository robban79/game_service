#!/usr/bin/env python3

from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

from user import UserApi
from message import MessageApi

app = Flask(__name__)
api = Api(app)

if __name__ == '__main__':
    api.add_resource(UserApi, "/user/")
    api.add_resource(MessageApi, "/message/")
    app.run(debug=True, host='0.0.0.0')
