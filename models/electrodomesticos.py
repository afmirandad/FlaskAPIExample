from models.db import db
import logging

logger = logging.getLogger(__name__)

class Electrodomestico(db.Model):
    __tablename__ = 'electrodomesticos'
    
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(100), nullable=False) # Ej: "Samsung", "LG"
    modelo = db.Column(db.String(100), nullable=False, unique=True) # Ej: "Nevera RF28R7351SG"
    tipo = db.Column(db.String(80), nullable=False) # Ej: "Nevera", "Lavadora", "Microondas"
    precio = db.Column(db.Float, nullable=False) # Precio de venta
    
    clase_energetica = db.Column(db.String(5), nullable=True) # Ej: "A++", "B"
    
    en_stock = db.Column(db.Boolean, default=True) 

    def __repr__(self):
        """
        Representación legible del objeto Electrodomestico.
        """
        return f'<Electrodomestico {self.marca} {self.modelo} ({self.tipo})>'