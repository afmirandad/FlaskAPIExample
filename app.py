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
import logging
from dotenv import load_dotenv


load_dotenv()

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)


logger.info('Inicializando la aplicación Flask')
app = Flask(__name__)


# Configuración de la base de datos y JWT desde .env
db_url = os.getenv('MYSQL_URL')
if db_url and db_url.startswith('mysql://'):
    db_url = db_url.replace('mysql://', 'mysql+pymysql://', 1)
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'tu_clave_secreta_jwt')
jwt = JWTManager(app)
logger.info(f"Conexión a la base de datos: {app.config['SQLALCHEMY_DATABASE_URI']}")

# Inicializar db con la app
db.init_app(app)
logger.info('SQLAlchemy inicializado')


# Endpoint raíz para información de la API
@app.route('/')
def index():
    return {
        "api": "FlaskAPIExample",
        "status": "OK",
        "description": "API RESTful con Flask, SQLAlchemy, JWT y estructura modular.",
        "author": "afmirandad",
        "endpoints": {
            "POST /users/register": "Registro de usuario",
            "POST /users/login": "Login y obtención de JWT",
            "GET /users/": "Listado de usuarios (requiere JWT)",
            "GET /": "Información de la API"
        },
        "repository": "https://github.com/afmirandad/FlaskAPIExample"
    }, 200

# Registrar blueprints de controladores
app.register_blueprint(user_bp)
logger.info('Blueprint de usuarios registrado')

if __name__ == '__main__':
    logger.info('Ejecutando como script principal')
    with app.app_context():
        db.create_all()  # Crea las tablas si no existen
        logger.info('Tablas creadas en la base de datos (si no existen)')

"""
Para agregar más controladores, importa y registra el blueprint correspondiente:
from controllers.otro_controller import otro_bp
app.register_blueprint(otro_bp)
"""
