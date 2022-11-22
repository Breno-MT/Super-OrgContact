import random
from flask_pymongo import PyMongo
from flask import current_app
from jwt import encode

mongo = PyMongo()

def generate_jwt(payload):
    token = encode(payload, current_app.config["SECRET_KEY"], "HS256")
    return token

def password_generator(): 
    letters = "abcdefghijklmnopqrstuvwxyzABCEFGHIJKLMNOPQRSTUVWXYZ123456789"
    caracter = '!@#$%&^*-_'

    password = ""

    for i in range(0, 1):
        password_caracter = random.choice(caracter)
        password += password_caracter
        for h in range(8, 17):
            password_letters = random.choice(letters)
            password += password_letters
    return password
