from flask import Flask
from src.controllers.user import users
from src.controllers.contacts import contacts

def routes(app: Flask):
    app.register_blueprint(users)
    app.register_blueprint(contacts)
