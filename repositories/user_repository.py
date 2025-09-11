"""
Repositorio para el modelo User.
Aquí se manejan las operaciones de acceso a datos para el modelo User.
Puedes crear más repositorios siguiendo este ejemplo.
"""


from sqlalchemy.orm import Session
from models.user import User
import logging

logger = logging.getLogger(__name__)

class UserRepository:
    @staticmethod
    def get_by_username(username, session: Session):
        logger.info(f'Buscando usuario en repositorio: {username}')
        user = session.query(User).filter_by(username=username).first()
        if user:
            logger.info(f'Usuario encontrado en repositorio: {username}')
        else:
            logger.warning(f'Usuario no encontrado en repositorio: {username}')
        return user

    @staticmethod
    def create_user(username, password, session: Session):
        logger.info(f'Creando usuario en repositorio: {username}')
        user = User(username=username, password=password)
        session.add(user)
        session.commit()
        logger.info(f'Usuario creado en repositorio: {username} (ID: {user.id})')
        return user

    @staticmethod
    def get_all(session: Session):
        logger.info('Obteniendo todos los usuarios en repositorio')
        users = session.query(User).all()
        logger.info(f'{len(users)} usuarios obtenidos en repositorio')
        return users

"""
Para crear más repositorios:
1. Crea un archivo en la carpeta repositories (ejemplo: product_repository.py).
2. Implementa métodos para acceder a los datos del modelo correspondiente.
"""
