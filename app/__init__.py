from flask import Flask
from . import main

def creat_app():
    app = Flask(__name__)
    app.config(['SECRET_KEY']) = '#######'
    app.register_blueprint(main)
    return main