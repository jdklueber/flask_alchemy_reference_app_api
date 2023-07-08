import os
from flask import Flask
from flask_smorest import Api
from db import db

# Importing these to make them available for sqlalchemy
import workflow_api.models


def create_app(db_url=None):
    app = Flask(__name__)

    ## FLASK CONFIG
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Workflow Tracker REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    ## SQLALCHEMY CONFIG
    default_data_file = r"C:\data\workflow_tracker.db"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv(
        "DATABASE_URL", f"sqlite:///{default_data_file}"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    # Probably omit this step for most enterprise applications
    with app.app_context():
        db.create_all()  # only creates tables that don't already exist

    api = Api(app)

    return app
