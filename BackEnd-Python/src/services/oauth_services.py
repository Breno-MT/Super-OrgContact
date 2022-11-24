import requests
import random
from flask import request, current_app
from flask.wrappers import Response
from werkzeug.utils import redirect
from flask.globals import session
from google import auth
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from src import mongo_client
from src.utils import generate_jwt
from src.services.user_services import create_oauth_user

def callback_google():

    flow.fetch_token(authorization_response = request.url)
    credentials = flow.credentials
    request_session = requests.session()
    token_google = auth.transport.requests.Request(session=request_session)

    user_google_dict = id_token.verify_oauth2_token(
        id_token = credentials.id_token,
        request=token_google,
        audience=current_app.config['GOOGLE_CLIENT_ID']
    )

    found_email = mongo_client.users.find_one({"email": user_google_dict["email"]})

    if found_email == None:

        create_oauth_user(user_google_dict["email"])

        session["google_id"] = user_google_dict.get("sub")

        del user_google_dict['aud']
        del user_google_dict['azp']

        token = generate_jwt(user_google_dict)

        return redirect(f"{current_app.config['FRONTEND_URL']}?jwt={token}")

    session["google_id"] = user_google_dict.get("sub")

    del user_google_dict['aud']
    del user_google_dict['azp']

    token = generate_jwt(user_google_dict)

    return redirect(f"{current_app.config['FRONTEND_URL']}?jwt={token}")

flow = Flow.from_client_secrets_file(
    client_secrets_file="src/database/client_secret.json",
    scopes=[
        "https://www.googleapis.com/auth/userinfo.email",
        "https://www.googleapis.com/auth/userinfo.profile",
        "https://www.googleapis.com/auth/contacts.readonly",
        "openid"
    ],
    redirect_uri = "http://localhost:5000/users/callback"
)
