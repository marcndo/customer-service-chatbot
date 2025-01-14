from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
