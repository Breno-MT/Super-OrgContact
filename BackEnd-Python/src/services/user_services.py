import bcrypt
from src import mongo_client
from src.utils import password_generator


def create_oauth_user(email):

    password_user = password_generator()

    try:
        if "@conectanuvem" in email:
            user_creation = {
                "email": email,
                "password": encrypt_password(password_user.encode("utf-8")),
                "domain": "ConectaNuvem"
            }
            mongo_client.users.insert_one(user_creation)

        if "@gmail" in email:
            user_creation = {
                "email": email,
                "password": encrypt_password(password_user.encode("utf-8")),
                "domain": "Gmail"
            }
            mongo_client.users.insert_one(user_creation)

    except Exception as e:
        return e

def encrypt_password(password):
    return bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf-8')

def check_password(password):
    return bcrypt.checkpw(password.encode("utf-8"), password.encode("utf-8"))
