"""
Modelo de usuario para SQLAlchemy.
Puedes crear más modelos siguiendo este ejemplo y agregarlos en la carpeta models.
"""
from models.db import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

"""
Para crear más modelos:
1. Crea un archivo en la carpeta models (ejemplo: product.py).
2. Define la clase heredando de db.Model.
3. Agrega los campos necesarios.
"""
