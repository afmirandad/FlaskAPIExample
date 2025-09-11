"""
Controlador para el modelo User.
Define los endpoints REST y de autenticación para usuarios.
Puedes crear más controladores siguiendo este ejemplo.
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from services.user_service import UserService
import logging

logger = logging.getLogger(__name__)

user_bp = Blueprint('user_bp', __name__, url_prefix='/users')

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    logger.info(f'Registrando usuario: {username}')
    user = UserService.register_user(username, password)
    logger.info(f'Usuario registrado: {user.username} (ID: {user.id})')
    return jsonify({'id': user.id, 'username': user.username}), 201

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    logger.info(f'Intento de login para usuario: {username}')
    user = UserService.authenticate(username, password)
    if user:
        access_token = create_access_token(identity=str(user.id))  # identity debe ser string
        logger.info(f'Login exitoso para usuario: {username}')
        return jsonify({'access_token': access_token}), 200
    logger.warning(f'Login fallido para usuario: {username}')
    return jsonify({'msg': 'Credenciales inválidas'}), 401

@user_bp.route('/', methods=['GET'])
@jwt_required()
def get_users():
    try:
        logger.info('Consultando listado de usuarios')
        users = UserService.get_all_users()
        logger.info(f'{len(users)} usuarios encontrados')
        return jsonify([{'id': u.id, 'username': u.username} for u in users]), 200
    except Exception as e:
        logger.error(f'Error al consultar usuarios: {str(e)}')
        return jsonify({'error': 'No autenticado', 'msg': str(e)}), 401

"""
Para crear más controladores:
1. Crea un archivo en la carpeta controllers (ejemplo: product_controller.py).
2. Define un Blueprint y los endpoints necesarios.
3. Registra el blueprint en app.py.
"""
