"""
Repositorio para el modelo User.
Aquí se manejan las operaciones de acceso a datos para el modelo User.
Puedes crear más repositorios siguiendo este ejemplo.
"""

from models.user import User
from models.db import db
import logging

logger = logging.getLogger(__name__)

class UserRepository:
    @staticmethod
    def get_by_username(username):
        logger.info(f'Buscando usuario en repositorio: {username}')
        user = User.query.filter_by(username=username).first()
        if user:
            logger.info(f'Usuario encontrado en repositorio: {username}')
        else:
            logger.warning(f'Usuario no encontrado en repositorio: {username}')
        return user

    @staticmethod
    def create_user(username, password):
        logger.info(f'Creando usuario en repositorio: {username}')
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        logger.info(f'Usuario creado en repositorio: {username} (ID: {user.id})')
        return user

    @staticmethod
    def get_all():
        logger.info('Obteniendo todos los usuarios en repositorio')
        users = User.query.all()
        logger.info(f'{len(users)} usuarios obtenidos en repositorio')
        return users

"""
Para crear más repositorios:
1. Crea un archivo en la carpeta repositories (ejemplo: product_repository.py).
2. Implementa métodos para acceder a los datos del modelo correspondiente.
"""
