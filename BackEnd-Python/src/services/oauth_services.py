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

    session["google_id"] = user_google_dict.get("sub")

    del user_google_dict['aud']
    del user_google_dict['azp']

    token = generate_jwt(user_google_dict)

    print(token)

    return redirect(f"{current_app.config['FRONTEND_URL']}?jwt={token}")


flow = Flow.from_client_secrets_file(
    client_secrets_file="src/database/client_secret.json",
    scopes=[
        "https://www.googleapis.com/auth/contacts.readonly",
        "https://www.googleapis.com/auth/userinfo.profile",
        "openid"
    ],
    redirect_uri = "http://localhost:5000/users/callback"
)

def password_generator(): 
    letters = "abcdefghijklmnopqrstuvwxyzABCEFGHIJKLMNOPQRSTUVWXYZ123456789"
    caracter = '!@#$%&^*-_'

    password = ""

    for i in range(0, 1):
        password_caracter = random.choice(caracter)
        password += password_caracter
        for h in range(0, 14):
            password_letters = random.choice(letters)
            password += password_letters
    return password
