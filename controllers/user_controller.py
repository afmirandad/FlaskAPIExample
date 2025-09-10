"""
Controlador para el modelo User.
Define los endpoints REST y de autenticación para usuarios.
Puedes crear más controladores siguiendo este ejemplo.
"""
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from services.user_service import UserService

user_bp = Blueprint('user_bp', __name__, url_prefix='/users')

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = UserService.register_user(username, password)
    return jsonify({'id': user.id, 'username': user.username}), 201

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = UserService.authenticate(username, password)
    if user:
        access_token = create_access_token(identity=str(user.id))  # identity debe ser string
        return jsonify({'access_token': access_token}), 200
    return jsonify({'msg': 'Credenciales inválidas'}), 401

@user_bp.route('/', methods=['GET'])
@jwt_required()
def get_users():
    users = UserService.get_all_users()
    return jsonify([{'id': u.id, 'username': u.username} for u in users])

"""
Para crear más controladores:
1. Crea un archivo en la carpeta controllers (ejemplo: product_controller.py).
2. Define un Blueprint y los endpoints necesarios.
3. Registra el blueprint en app.py.
"""
