from bson import json_util
from flask import Blueprint, request, json
from flask.wrappers import Response
from flask.globals import session
from google import auth
from google.oauth2 import id_token
from src.services.oauth_services import callback_google, flow

users = Blueprint("users", __name__, url_prefix="/users")

@users.route("/", methods=["GET"])
def get_users():
    return Response(
        response=json_util.dumps({"records": "ok"}),
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
