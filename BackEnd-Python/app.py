from src import app
from src.routes import routes

routes(app=app)

if __name__ == "__main__":
    app.run()