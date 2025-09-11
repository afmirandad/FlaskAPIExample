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
    """
    Registro de usuario
    ---
    tags:
      - Usuarios
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [username, password]
          properties:
            username:
              type: string
              example: usuario1
            password:
              type: string
              example: "Secreta123!"
    responses:
      201:
        description: Usuario registrado exitosamente
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            username:
              type: string
              example: usuario1
      400:
        description: Petición inválida
        schema:
          type: object
          properties:
            msg:
              type: string
              example: "username y password son requeridos"
      409:
        description: Usuario ya existe
        schema:
          type: object
          properties:
            msg:
              type: string
              example: "Usuario ya existe"
      500:
        description: Error interno al registrar
        schema:
          type: object
          properties:
            msg:
              type: string
              example: "No se pudo completar el registro"
    """
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({"msg": "username y password son requeridos"}), 400

    try:
        logger.info(f'Registrando usuario: {username}')
        user = UserService.register_user(username, password)

        # Soporta contrato donde el servicio devuelve dict de error
        if isinstance(user, dict) and user.get('error') == 'Usuario ya existe':
            logger.warning(f'Usuario ya existe: {username}')
            return jsonify({'msg': 'Usuario ya existe'}), 409

        logger.info(f'Usuario registrado: {user.username} (ID: {user.id})')
        return jsonify({'id': user.id, 'username': user.username}), 201

    except Exception as e:
        logger.exception("Error en registro de usuario")
        return jsonify({'msg': 'No se pudo completar el registro', 'detail': str(e)}), 500


@user_bp.route('/login', methods=['POST'])
def login():
    """
    Login de usuario
    ---
    tags:
      - Usuarios
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [username, password]
          properties:
            username:
              type: string
              example: usuario1
            password:
              type: string
              example: "Secreta123!"
    responses:
      200:
        description: Login exitoso y retorno de JWT
        schema:
          type: object
          properties:
            access_token:
              type: string
              example: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
      400:
        description: Petición inválida
        schema:
          type: object
          properties:
            msg:
              type: string
              example: "username y password son requeridos"
      401:
        description: Credenciales inválidas
        schema:
          type: object
          properties:
            msg:
              type: string
              example: "Credenciales inválidas"
    """
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({"msg": "username y password son requeridos"}), 400

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
    """
    Listado de usuarios (requiere JWT)
    ---
    tags:
      - Usuarios
    security:
      - Bearer: []
    responses:
      200:
        description: Listado de usuarios
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              username:
                type: string
                example: usuario1
        examples:
          application/json:
            - id: 1
              username: usuario1
            - id: 2
              username: usuario2
      401:
        description: No autenticado
        schema:
          type: object
          properties:
            error:
              type: string
              example: "No autenticado"
            msg:
              type: string
              example: "Token inválido"
    """
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
