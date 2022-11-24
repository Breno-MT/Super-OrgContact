from bson import json_util
from flask import Blueprint, request, json
from flask.wrappers import Response
from src.services.people_api_services import people_api_paginate_10
from src.services.people_api_services import people_api_all_person_connection

contacts = Blueprint("contacts", __name__, url_prefix="/contacts")

@contacts.route("/people_api/v1/get_all_connections", methods=["GET"])
def get_all_person_connections():
    """
    From the Authenticated User, get all connections.
    """
    return Response(
        response=json_util.dumps(people_api_all_person_connection()),
        status=200,
        mimetype="application/json"
    )

@contacts.route("/people_api/v1/list_10_connections", methods=["GET"])
def list_10_person_connection():
    """
    From the Authenticated User, list up to 10 person connections.
    """
    return Response(
        response=json_util.dumps(people_api_paginate_10()),
        status=200,
        mimetype="application/json"
    )
