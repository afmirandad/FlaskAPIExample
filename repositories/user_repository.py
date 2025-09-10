"""
Repositorio para el modelo User.
Aquí se manejan las operaciones de acceso a datos para el modelo User.
Puedes crear más repositorios siguiendo este ejemplo.
"""
from models.user import User
from models.db import db

class UserRepository:
    @staticmethod
    def get_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def create_user(username, password):
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_all():
        return User.query.all()

"""
Para crear más repositorios:
1. Crea un archivo en la carpeta repositories (ejemplo: product_repository.py).
2. Implementa métodos para acceder a los datos del modelo correspondiente.
"""
