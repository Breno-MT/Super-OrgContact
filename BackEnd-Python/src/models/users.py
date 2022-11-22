users_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["_id", "email", "password", "domain"],
        "properties": {
            "_id": {
                "bsonType": "objectId",
                "description": "Chave definida da collection",
            },
            "email": {
                "bsonType": "string",
                "pattern": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+[.]+[a-zA-Z]{2,10}$",
                "description": "Email do usuário",
            },
            "password": {
                "bsonType": "string",
                "pattern": "^[a-zA-Z0-9.!@#$%&*/_%+-]{8,99}$",
                "description": "Senha do usuário",
            },
            "domain": {
                "bsonType": "string",
                "description": "Vinculo da domain gmail",
            },
        },
    }
}

def create_collection_users(mongo_client):
    try:
        print("Criando Users collection.")
        mongo_client.create_collection("users")
        print("Users criada com sucesso.")

    except Exception as e:
        print(e)

    mongo_client.command("collMod", "users", validator=users_validator)
