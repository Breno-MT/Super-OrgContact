from bson import json_util
from flask import Blueprint, request, json
from flask.wrappers import Response
from flask.globals import session
from google import auth
from google.oauth2 import id_token
from src.services.oauth_services import callback_google, flow
from src.services.people_api_services import people_api_paginate_10
from src.services.people_api_services import people_api_all_person_connection

users = Blueprint("users", __name__, url_prefix="/users")

@users.route("/people_api/v1/get_all_connections", methods=["GET"])
def get_all_person_connections():
    """
    From the Authenticated User, get all connections.
    """
    return Response(
        response=json_util.dumps(people_api_all_person_connection()),
        status=200,
        mimetype="application/json"
    )

@users.route("/people_api/v1/list_10_connections", methods=["GET"])
def list_10_person_connection():
    """
    From the Authenticated User, list up to 10 person connections.
    """
    return Response(
        response=json_util.dumps(people_api_paginate_10()),
        status=200,
        mimetype="application/json"
    )

@users.route("/auth/google", methods=["POST"])
def auth_google():

    authorization_url, state = flow.authorization_url()
    session["state"] = state

    return Response(
        response=json.dumps({'url':authorization_url}),
        status=200,
        mimetype='application/json'
    )

@users.route("/callback", methods=["GET"])
def callback():
    return callback_google()
