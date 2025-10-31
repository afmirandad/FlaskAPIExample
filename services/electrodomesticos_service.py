from repositories.electrodomesticos_repository import ElectrodomesticosRepository
from werkzeug.security import generate_password_hash, check_password_hash
import logging

logger = logging.getLogger(__name__)

class ElectrodomesticosService:
    
    @staticmethod
    def create_electrodomestico(electrodomestico_data):
        from models.db import db
        logger.info(f'Creando electrodoméstico en servicio: {electrodomestico_data.get("marca")} {electrodomestico_data.get("modelo")}')
        electrodomestico = ElectrodomesticosRepository.create(electrodomestico_data, db.session)
        logger.info(f'Electrodoméstico creado en servicio: {electrodomestico.modelo} (ID: {electrodomestico.id})')
        return electrodomestico


    @staticmethod
    def get_electrodomestico_by_id(electrodomestico_id):
        from models.db import db
        logger.info(f'Obteniendo electrodoméstico por ID en servicio: {electrodomestico_id}')
        electrodomestico = ElectrodomesticosRepository.get_by_id(electrodomestico_id, db.session)
        if electrodomestico:
            logger.info(f'Electrodoméstico obtenido en servicio: {electrodomestico.modelo}')
        else:
            logger.warning(f'Electrodoméstico no encontrado en servicio con ID: {electrodomestico_id}')
        return electrodomestico

    @staticmethod
    def get_electrodomestico_by_modelo(modelo):
        from models.db import db
        logger.info(f'Obteniendo electrodoméstico por modelo en servicio: {modelo}')
        electrodomestico = ElectrodomesticosRepository.get_by_modelo(modelo, db.session)
        if electrodomestico:
            logger.info(f'Electrodoméstico obtenido en servicio: {electrodomestico.modelo}')
        else:
            logger.warning(f'Electrodoméstico no encontrado en servicio con modelo: {modelo}')
        return electrodomestico

    @staticmethod
    def get_all_electrodomesticos():
        from models.db import db
        logger.info('Obteniendo todos los electrodomésticos en servicio')
        electrodomesticos = ElectrodomesticosRepository.get_all(db.session)
        logger.info(f'{len(electrodomesticos)} electrodomésticos obtenidos en servicio')
        return electrodomesticos

    @staticmethod
    def update_electrodomestico(electrodomestico_id, update_data):
        from models.db import db
        logger.info(f'Actualizando electrodoméstico en servicio: ID {electrodomestico_id}')
        electrodomestico = ElectrodomesticosRepository.update(electrodomestico_id, update_data, db.session)
        if electrodomestico:
            logger.info(f'Electrodoméstico actualizado en servicio: {electrodomestico.modelo} (ID: {electrodomestico.id})')
        else:
            logger.warning(f'No se pudo actualizar el electrodoméstico en servicio con ID: {electrodomestico_id}')
        return electrodomestico

    @staticmethod
    def delete_electrodomestico(electrodomestico_id):
        from models.db import db
        logger.info(f'Eliminando electrodoméstico en servicio: ID {electrodomestico_id}')
        result = ElectrodomesticosRepository.delete(electrodomestico_id, db.session)
        if result:
            logger.info(f'Electrodoméstico eliminado en servicio: ID {electrodomestico_id}')
        else:
            logger.warning(f'No se pudo eliminar el electrodoméstico en servicio con ID: {electrodomestico_id}')
        return result