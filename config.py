import os
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

MONGO_URL = os.environ.get('MONGODB_URI')
client = MongoClient(MONGO_URL)

db = client.heroku_t0z9f65z

try:
	app.config.from_pyfile("dev_config.cfg")
	app.config['SERVER'] = 'local'
	print(">>> Development configuration file loaded.")
	app.config['DEBUG'] = True
except:
	app.config['SERVER'] = 'production'
	app.config['DEBUG'] = False
	app.config['SECRET_KEY'] = os.environ['SECRET_KEY']