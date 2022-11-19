import os
from flask import Flask
from flask_cors import CORS
from src.config import app_config
from src.utils import mongo


def create_app(enviroment):

    global mongo_client

    app = Flask(__name__)
    app.config.from_object(app_config[enviroment])
    mongo.init_app(app)
    mongo_client = mongo.db
    CORS(app)

    return app

app = create_app(os.getenv("FLASK_ENV"))
