# FlaskAPIExample

## Descripción
Este proyecto es una API REST desarrollada en Python usando Flask, SQLAlchemy y MySQL, con autenticación JWT. La estructura está organizada en módulos: controllers, models, services y repositories, facilitando la escalabilidad y el mantenimiento.

### Estructura de carpetas
- **controllers/**: Define los endpoints y la lógica de las rutas.
- **models/**: Define los modelos de datos (ORM).
- **services/**: Contiene la lógica de negocio.
- **repositories/**: Encapsula el acceso a la base de datos.

Cada carpeta contiene un archivo `__init__.py` para ser reconocida como módulo.

## Instalación
1. Clona el repositorio.
2. Instala las dependencias:
	```bash
	pip install flask flask_sqlalchemy flask_jwt_extended pymysql werkzeug
	```
3. Configura la conexión a MySQL en `app.py`.
4. Ejecuta la aplicación:
	```bash
	python app.py
	```

## Extensión
Para agregar nuevos modelos, servicios, repositorios y controladores, sigue los ejemplos y comentarios en cada archivo.

## Endpoints principales
- `POST /users/register`: Registro de usuario.
- `POST /users/login`: Autenticación y obtención de JWT.
- `GET /users/`: Listado de usuarios (requiere JWT).

## Autenticación
La autenticación se realiza mediante JWT. Al iniciar sesión, se obtiene un token que debe enviarse en el header `Authorization` para acceder a rutas protegidas.

## Comentarios
Cada archivo contiene instrucciones y ejemplos para extender la API.
# FlaskAPIExample