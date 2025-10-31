from sqlalchemy.orm import Session
from models.electrodomesticos import Electrodomestico
import logging

logger = logging.getLogger(__name__)

class ElectrodomesticoRepository:
    @staticmethod
    def create(electrodomestico_data, session: Session):
        """
        Crea un nuevo electrodoméstico en la base de datos.
        
        Args:
            electrodomestico_data (dict): Diccionario con los datos del electrodoméstico
            session (Session): Sesión de SQLAlchemy
            
        Returns:
            Electrodomestico: El electrodoméstico creado
        """
        logger.info(f'Creando electrodoméstico en repositorio: {electrodomestico_data.get("marca")} {electrodomestico_data.get("modelo")}')
        electrodomestico = Electrodomestico(
            marca=electrodomestico_data.get('marca'),
            modelo=electrodomestico_data.get('modelo'),
            tipo=electrodomestico_data.get('tipo'),
            precio=electrodomestico_data.get('precio'),
            clase_energetica=electrodomestico_data.get('clase_energetica'),
            en_stock=electrodomestico_data.get('en_stock', True)
        )
        session.add(electrodomestico)
        session.commit()
        logger.info(f'Electrodoméstico creado en repositorio: {electrodomestico.modelo} (ID: {electrodomestico.id})')
        return electrodomestico
    
    @staticmethod
    def get_by_id(electrodomestico_id, session: Session):
        """
        Obtiene un electrodoméstico por su ID.
        
        Args:
            electrodomestico_id (int): ID del electrodoméstico
            session (Session): Sesión de SQLAlchemy
            
        Returns:
            Electrodomestico: El electrodoméstico encontrado o None
        """
        logger.info(f'Buscando electrodoméstico por ID en repositorio: {electrodomestico_id}')
        electrodomestico = session.query(Electrodomestico).filter_by(id=electrodomestico_id).first()
        if electrodomestico:
            logger.info(f'Electrodoméstico encontrado en repositorio: {electrodomestico.modelo}')
        else:
            logger.warning(f'Electrodoméstico no encontrado en repositorio con ID: {electrodomestico_id}')
        return electrodomestico
    
    @staticmethod
    def get_by_modelo(modelo, session: Session):
        """
        Obtiene un electrodoméstico por su modelo.
        
        Args:
            modelo (str): Modelo del electrodoméstico
            session (Session): Sesión de SQLAlchemy
            
        Returns:
            Electrodomestico: El electrodoméstico encontrado o None
        """
        logger.info(f'Buscando electrodoméstico por modelo en repositorio: {modelo}')
        electrodomestico = session.query(Electrodomestico).filter_by(modelo=modelo).first()
        if electrodomestico:
            logger.info(f'Electrodoméstico encontrado en repositorio: {electrodomestico.modelo}')
        else:
            logger.warning(f'Electrodoméstico no encontrado en repositorio con modelo: {modelo}')
        return electrodomestico
    
    @staticmethod
    def get_all(session: Session):
        """
        Obtiene todos los electrodomésticos.
        
        Args:
            session (Session): Sesión de SQLAlchemy
            
        Returns:
            list: Lista de todos los electrodomésticos
        """
        logger.info('Obteniendo todos los electrodomésticos en repositorio')
        electrodomesticos = session.query(Electrodomestico).all()
        logger.info(f'{len(electrodomesticos)} electrodomésticos obtenidos en repositorio')
        return electrodomesticos
    
    @staticmethod
    def get_by_tipo(tipo, session: Session):
        """
        Obtiene todos los electrodomésticos de un tipo específico.
        
        Args:
            tipo (str): Tipo de electrodoméstico (Ej: "Nevera", "Lavadora")
            session (Session): Sesión de SQLAlchemy
            
        Returns:
            list: Lista de electrodomésticos del tipo especificado
        """
        logger.info(f'Buscando electrodomésticos por tipo en repositorio: {tipo}')
        electrodomesticos = session.query(Electrodomestico).filter_by(tipo=tipo).all()
        logger.info(f'{len(electrodomesticos)} electrodomésticos del tipo "{tipo}" encontrados')
        return electrodomesticos
    
    @staticmethod
    def get_by_marca(marca, session: Session):
        """
        Obtiene todos los electrodomésticos de una marca específica.
        
        Args:
            marca (str): Marca del electrodoméstico
            session (Session): Sesión de SQLAlchemy
            
        Returns:
            list: Lista de electrodomésticos de la marca especificada
        """
        logger.info(f'Buscando electrodomésticos por marca en repositorio: {marca}')
        electrodomesticos = session.query(Electrodomestico).filter_by(marca=marca).all()
        logger.info(f'{len(electrodomesticos)} electrodomésticos de la marca "{marca}" encontrados')
        return electrodomesticos
    
    @staticmethod
    def get_in_stock(session: Session):
        """
        Obtiene todos los electrodomésticos que están en stock.
        
        Args:
            session (Session): Sesión de SQLAlchemy
            
        Returns:
            list: Lista de electrodomésticos en stock
        """
        logger.info('Obteniendo electrodomésticos en stock en repositorio')
        electrodomesticos = session.query(Electrodomestico).filter_by(en_stock=True).all()
        logger.info(f'{len(electrodomesticos)} electrodomésticos en stock encontrados')
        return electrodomesticos
    
    @staticmethod
    def get_by_price_range(min_price, max_price, session: Session):
        """
        Obtiene electrodomésticos dentro de un rango de precio.
        
        Args:
            min_price (float): Precio mínimo
            max_price (float): Precio máximo
            session (Session): Sesión de SQLAlchemy
            
        Returns:
            list: Lista de electrodomésticos en el rango de precio
        """
        logger.info(f'Buscando electrodomésticos por rango de precio: {min_price} - {max_price}')
        electrodomesticos = session.query(Electrodomestico).filter(
            Electrodomestico.precio >= min_price,
            Electrodomestico.precio <= max_price
        ).all()
        logger.info(f'{len(electrodomesticos)} electrodomésticos encontrados en el rango de precio')
        return electrodomesticos
    
    @staticmethod
    def update(electrodomestico_id, electrodomestico_data, session: Session):
        """
        Actualiza un electrodoméstico existente.
        
        Args:
            electrodomestico_id (int): ID del electrodoméstico a actualizar
            electrodomestico_data (dict): Diccionario con los datos a actualizar
            session (Session): Sesión de SQLAlchemy
            
        Returns:
            Electrodomestico: El electrodoméstico actualizado o None si no existe
        """
        logger.info(f'Actualizando electrodoméstico en repositorio: ID {electrodomestico_id}')
        electrodomestico = session.query(Electrodomestico).filter_by(id=electrodomestico_id).first()
        
        if not electrodomestico:
            logger.warning(f'Electrodoméstico no encontrado para actualizar con ID: {electrodomestico_id}')
            return None
        
        # Actualizar solo los campos proporcionados
        if 'marca' in electrodomestico_data:
            electrodomestico.marca = electrodomestico_data['marca']
        if 'modelo' in electrodomestico_data:
            electrodomestico.modelo = electrodomestico_data['modelo']
        if 'tipo' in electrodomestico_data:
            electrodomestico.tipo = electrodomestico_data['tipo']
        if 'precio' in electrodomestico_data:
            electrodomestico.precio = electrodomestico_data['precio']
        if 'clase_energetica' in electrodomestico_data:
            electrodomestico.clase_energetica = electrodomestico_data['clase_energetica']
        if 'en_stock' in electrodomestico_data:
            electrodomestico.en_stock = electrodomestico_data['en_stock']
        
        session.commit()
        logger.info(f'Electrodoméstico actualizado en repositorio: {electrodomestico.modelo} (ID: {electrodomestico.id})')
        return electrodomestico
    
    @staticmethod
    def delete(electrodomestico_id, session: Session):
        """
        Elimina un electrodoméstico por su ID.
        
        Args:
            electrodomestico_id (int): ID del electrodoméstico a eliminar
            session (Session): Sesión de SQLAlchemy
            
        Returns:
            bool: True si se eliminó correctamente, False si no existe
        """
        logger.info(f'Eliminando electrodoméstico en repositorio: ID {electrodomestico_id}')
        electrodomestico = session.query(Electrodomestico).filter_by(id=electrodomestico_id).first()
        
        if not electrodomestico:
            logger.warning(f'Electrodoméstico no encontrado para eliminar con ID: {electrodomestico_id}')
            return False
        
        session.delete(electrodomestico)
        session.commit()
        logger.info(f'Electrodoméstico eliminado en repositorio: ID {electrodomestico_id}')
        return True