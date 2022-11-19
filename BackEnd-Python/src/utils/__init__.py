from flask_pymongo import PyMongo
from flask import current_app
from jwt import encode

mongo = PyMongo()

def generate_jwt(payload):
    token = encode(payload, current_app.config["SECRET_KEY"], "HS256")
    return token