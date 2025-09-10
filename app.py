"""
Archivo principal de la aplicación Flask.
Configura la conexión a MySQL, JWT y registra los blueprints de los controladores.
"""
from flask import Flask
from flask import Flask
from flask_jwt_extended import JWTManager
from controllers.user_controller import user_bp
from models.db import db
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configuración de la base de datos y JWT desde .env
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///flaskapi.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'tu_clave_secreta_jwt')
jwt = JWTManager(app)

# Inicializar db con la app
db.init_app(app)

# Registrar blueprints de controladores
app.register_blueprint(user_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crea las tablas si no existen

"""
Para agregar más controladores, importa y registra el blueprint correspondiente:
from controllers.otro_controller import otro_bp
app.register_blueprint(otro_bp)
"""
