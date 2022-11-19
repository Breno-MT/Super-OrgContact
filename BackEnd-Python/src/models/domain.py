domain_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["_id","name"],
        "properties": {
            "_id": {
                "bsonType": "objectId",
                "description": "Chave definida da collection"
            },
            "name": {
                "bsonType": "string",
                "description": "Nome da domain",
            },
        },
    }
  }

def create_collection_domain(mongo_client):
    try:
        print("Criando Domain collection.")
        mongo_client.create_collection("domain")
        print("Domain criada com sucesso.")

    except Exception as e:
        print(e)

    mongo_client.command("collMod", "domain", validator=domain_validator)
