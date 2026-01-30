from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

load_dotenv()


# print(os.getenv('MONGODB_URI'))

# Setup MongoDB here
# mongo = PyMongo(uri="mongodb://localhost:27017/database")

mongo = PyMongo(uri=os.getenv('MONGODB_URI'))


def mongodb_init(app):
    mongodb_uri = os.getenv('MONGODB_URI')

    app.config['MONGO_URI'] = mongodb_uri
    mongo.init_app(app)

    return mongo
