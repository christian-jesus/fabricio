# app/__init__.py
from flask import Flask
from flask_cors import CORS
from .routes import main

def create_app():
    app = Flask(__name__)
    CORS(app)  # Habilitar CORS para todas las rutas y orígenes
    app.register_blueprint(main)
    return app
