from flask import Flask
from src.controllers.user import users

def routes(app: Flask):
    app.register_blueprint(users)
