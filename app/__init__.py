from flask import Flask
from app.webhook.routes import webhook
from .extensions import mongo, mongodb_init
from dotenv import load_dotenv
import os

load_dotenv()


# Creating our flask app
def create_app():

    app = Flask(__name__)
    
    # DB init
    mongodb_init(app)

    # registering all the blueprints
    app.register_blueprint(webhook)
    
    return app
