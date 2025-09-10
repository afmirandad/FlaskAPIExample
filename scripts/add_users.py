"""
Script para agregar usuarios de ejemplo a la base de datos SQLite.
Ejecuta este archivo para poblar la tabla users.
"""
import os
from models.db import db
from models.user import User
from werkzeug.security import generate_password_hash
from flask import Flask
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///flaskapi.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

usuarios = [
    {"username": "usuario1", "password": "password1"},
    {"username": "usuario2", "password": "password2"},
    {"username": "usuario3", "password": "password3"}
]

with app.app_context():
    db.create_all()
    for u in usuarios:
        if not User.query.filter_by(username=u["username"]).first():
            user = User(username=u["username"], password=generate_password_hash(u["password"]))
            db.session.add(user)
    db.session.commit()
print("Usuarios agregados correctamente.")
