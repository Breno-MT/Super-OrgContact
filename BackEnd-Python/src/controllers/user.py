from bson import json_util
from flask import Blueprint, request, json
from flask.wrappers import Response
from flask.globals import session
from google import auth
from google.oauth2 import id_token
from src.services.oauth_services import callback_google, flow
from src import mongo_client

users = Blueprint("users", __name__, url_prefix="/users")

@users.route("/get_domain_conecta", methods=["GET"])
def get_domain_conecta_nuvem():

    response = mongo_client.users.aggregate([
        {
            '$match': {
                'domain': 'ConectaNuvem'
            }
        }
    ])

    if response == []:
        return Response(
            response=json_util.dumps({"error": "Não tem nenhum email com esse domínio."}),
            status=404,
            mimetype="application/json"
        )

    return Response(
        response=json_util.dumps(response),
        status=200,
        mimetype="application/json"
    )

@users.route("/get_domain_gmail", methods=["GET"])
def get_domain_gmail():

    response = mongo_client.users.aggregate([
        {
            '$match': {
                'domain': 'Gmail'
            }
        }
    ])

    if response == []:
        return Response(
            response=json_util.dumps({"error": "Não tem nenhum email com esse domínio."}),
            status=404,
            mimetype="application/json"
        )

    return Response(
        response=json_util.dumps(response),
        status=200,
        mimetype="application/json"
    )


@users.route("/auth/google", methods=["POST"])
def auth_google():

    authorization_url, state = flow.authorization_url()
    session["state"] = state

    return Response(
        response=json_util.dumps({'url':authorization_url}),
        status=200,
        mimetype='application/json'
    )

@users.route("/callback", methods=["GET"])
def callback(): return callback_google()
