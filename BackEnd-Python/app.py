import click
from flask.cli import with_appcontext
from src import app, mongo_client
from src.routes import routes
from src.models.users import create_collection_users
from src.models.domain import create_collection_domain

routes(app=app)

@click.command(name="create_collections")
@with_appcontext
def command_collection():
    create_collection_users(mongo_client)
    create_collection_domain(mongo_client)

app.cli.add_command(command_collection)

if __name__ == "__main__":
    app.run()
