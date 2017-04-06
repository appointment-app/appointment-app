import os
from flask import Flask

app = Flask(__name__)

try:
	app.config.from_pyfile("dev_config.cfg")
	app.config['SERVER'] = 'local'
	print(">>> Development configuration file loaded.")
	app.config['DEBUG'] = True
	print app.config
except:
	pass
