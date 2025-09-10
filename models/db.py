"""
Archivo para inicializar el objeto db de SQLAlchemy.
Importa este objeto en los modelos y repositorios para evitar ciclos de importación.
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
