"""
Servicio para el modelo User.
Aquí se maneja la lógica de negocio relacionada con usuarios.
Puedes crear más servicios siguiendo este ejemplo.
"""
from repositories.user_repository import UserRepository
from werkzeug.security import generate_password_hash, check_password_hash

class UserService:
    @staticmethod
    def register_user(username, password):
        hashed_password = generate_password_hash(password)
        return UserRepository.create_user(username, hashed_password)

    @staticmethod
    def authenticate(username, password):
        user = UserRepository.get_by_username(username)
        if user and check_password_hash(user.password, password):
            return user
        return None

    @staticmethod
    def get_all_users():
        return UserRepository.get_all()

"""
Para crear más servicios:
1. Crea un archivo en la carpeta services (ejemplo: product_service.py).
2. Implementa la lógica de negocio para el modelo correspondiente.
"""
