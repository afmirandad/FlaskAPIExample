from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from services.electrodomesticos_service import ElectrodomesticosService
import logging

logger = logging.getLogger(__name__)

electrodomesticos_bp = Blueprint('electrodomesticos_bp', __name__, url_prefix='/electrodomesticos')

@electrodomesticos_bp.route('/', methods=['POST'])
@jwt_required()
def create_electrodomestico():
    """
    Crear un nuevo electrodoméstico
    ---
    tags:
      - Electrodomésticos
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [marca, modelo, tipo, precio]
          properties:
            marca:
              type: string
              example: Samsung
            modelo:
              type: string
              example: Nevera RF28R7351SG
            tipo:
              type: string
              example: Nevera
            precio:
              type: number
              example: 1200.50
            clase_energetica:
              type: string
              example: A++
            en_stock:
              type: boolean
              example: true
    responses:
      201:
        description: Electrodoméstico creado exitosamente
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            marca:
              type: string
              example: Samsung
            modelo:
              type: string
              example: Nevera RF28R7351SG
            tipo:
              type: string
              example: Nevera
            precio:
              type: number
              example: 1200.50
            clase_energetica:
              type: string
              example: A++
            en_stock:
              type: boolean
              example: true
      400:
        description: Petición inválida
        schema:
          type: object
          properties:
            mensaje:
              type: string
              example: "Error en la petición"
        500:
          description: Error interno del servidor
          schema:
            type: object
            properties:
              mensaje:
                type: string
                example: "Error en el servidor"
    """
    data = request.get_json() or {}
    required_fields = ['marca', 'modelo', 'tipo', 'precio']
    if not all(field in data for field in required_fields):
        return jsonify({"mensaje": "Error en la petición"}), 400

    try:
        electrodomestico = ElectrodomesticosService.create_electrodomestico(data)
        response = {
            "id": electrodomestico.id,
            "marca": electrodomestico.marca,
            "modelo": electrodomestico.modelo,
            "tipo": electrodomestico.tipo,
            "precio": electrodomestico.precio,
            "clase_energetica": electrodomestico.clase_energetica,
            "en_stock": electrodomestico.en_stock
        }
        return jsonify(response), 201
    except Exception as e:
        logger.error(f'Error al crear el electrodoméstico: {str(e)}')
        return jsonify({"mensaje": "Error en el servidor"}), 500

@electrodomesticos_bp.route('/<int:electrodomestico_id>', methods=['GET'])
@jwt_required()
def get_electrodomestico(electrodomestico_id):
    """
    Obtener un electrodoméstico por ID
    ---
    tags:
      - Electrodomésticos
    parameters:
      - in: path
        name: electrodomestico_id
        required: true
        type: integer
        description: ID del electrodoméstico
    responses:
      200:
        description: Electrodoméstico obtenido exitosamente
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            marca:
              type: string
              example: Samsung
            modelo:
              type: string
              example: Nevera RF28R7351SG
            tipo:
              type: string
              example: Nevera
            precio:
              type: number
              example: 1200.50
            clase_energetica:
              type: string
              example: A++
            en_stock:
              type: boolean
              example: true
      404:
        description: Electrodoméstico no encontrado
        schema:
          type: object
          properties:
            mensaje:
              type: string
              example: "Electrodoméstico no encontrado"
        500:
          description: Error interno del servidor
          schema:
            type: object
            properties:
              mensaje:
                type: string
                example: "Error en el servidor"
    """
    try:
        electrodomestico = ElectrodomesticosService.get_electrodomestico_by_id(electrodomestico_id)
        if not electrodomestico:
            return jsonify({"mensaje": "Electrodoméstico no encontrado"}), 404

        response = {
            "id": electrodomestico.id,
            "marca": electrodomestico.marca,
            "modelo": electrodomestico.modelo,
            "tipo": electrodomestico.tipo,
            "precio": electrodomestico.precio,
            "clase_energetica": electrodomestico.clase_energetica,
            "en_stock": electrodomestico.en_stock
        }
        return jsonify(response), 200
    except Exception as e:
        logger.error(f'Error al obtener el electrodoméstico: {str(e)}')
        return jsonify({"mensaje": "Error en el servidor"}), 500

@electrodomesticos_bp.route('/', methods=['GET'])
@jwt_required()
def get_all_electrodomesticos():
    """
    Obtener todos los electrodomésticos
    ---
    tags:
      - Electrodomésticos
    responses:
      200:
        description: Lista de electrodomésticos obtenida exitosamente
        schema:
            type: array
            items:
              type: object
              properties:
                id:
                  type: integer
                  example: 1
                marca:
                  type: string
                  example: Samsung
                modelo:
                  type: string
                  example: Nevera RF28R7351SG
                tipo:
                  type: string
                  example: Nevera
                precio:
                  type: number
                  example: 1200.50
                clase_energetica:
                  type: string
                  example: A++
                en_stock:
                  type: boolean
                  example: true
      500:
        description: Error interno del servidor
        schema:
          type: object
          properties:
            mensaje:
              type: string
              example: "Error en el servidor"
    """
    try:
        electrodomesticos = ElectrodomesticosService.get_all_electrodomesticos()
        response = []
        for e in electrodomesticos:
            response.append({
                "id": e.id,
                "marca": e.marca,
                "modelo": e.modelo,
                "tipo": e.tipo,
                "precio": e.precio,
                "clase_energetica": e.clase_energetica,
                "en_stock": e.en_stock
            })
        return jsonify(response), 200
    except Exception as e:
        logger.error(f'Error al obtener los electrodomésticos: {str(e)}')
        return jsonify({"mensaje": "Error en el servidor"}), 500

@electrodomesticos_bp.route('/<int:electrodomestico_id>', methods=['PUT'])
@jwt_required()
def update_electrodomestico(electrodomestico_id):
    """
    Actualizar un electrodoméstico por ID
    ---
    tags:
      - Electrodomésticos
    consumes:
      - application/json
    parameters:
      - in: path
        name: electrodomestico_id
        required: true
        type: integer
        description: ID del electrodoméstico
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            marca:
              type: string
              example: Samsung
            modelo:
              type: string
              example: Nevera RF28R7351SG
            tipo:
              type: string
              example: Nevera
            precio:
              type: number
              example: 1200.50
            clase_energetica:
              type: string
              example: A++
            en_stock:
              type: boolean
              example: true
    responses:
      200:
        description: Electrodoméstico actualizado exitosamente
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            marca:
              type: string
              example: Samsung
            modelo:
              type: string
              example: Nevera RF28R7351SG
            tipo:
              type: string
              example: Nevera
            precio:
              type: number
              example: 1200.50
            clase_energetica:
              type: string
              example: A++
            en_stock:
              type: boolean
              example: true
      404:
        description: Electrodoméstico no encontrado
        schema:
          type: object
          properties:
            mensaje:
              type: string
              example: "Electrodoméstico no encontrado"
        500:
          description: Error interno del servidor
          schema:
            type: object
            properties:
              mensaje:
                type: string
                example: "Error en el servidor"
    """
    data = request.get_json() or {}
    try:
        electrodomestico = ElectrodomesticosService.update_electrodomestico(electrodomestico_id, data)
        if not electrodomestico:
            return jsonify({"mensaje": "Electrodoméstico no encontrado"}), 404

        response = {
            "id": electrodomestico.id,
            "marca": electrodomestico.marca,
            "modelo": electrodomestico.modelo,
            "tipo": electrodomestico.tipo,
            "precio": electrodomestico.precio,
            "clase_energetica": electrodomestico.clase_energetica,
            "en_stock": electrodomestico.en_stock
        }
        return jsonify(response), 200
    except Exception as e:
        logger.error(f'Error al actualizar el electrodoméstico: {str(e)}')
        return jsonify({"mensaje": "Error en el servidor"}), 500

@electrodomesticos_bp.route('/<int:electrodomestico_id>', methods=['DELETE'])
@jwt_required()
def delete_electrodomestico(electrodomestico_id):
    """
    Eliminar un electrodoméstico por ID
    ---
    tags:
      - Electrodomésticos
    parameters:
      - in: path
        name: electrodomestico_id
        required: true
        type: integer
        description: ID del electrodoméstico
    responses:
      200:
        description: Electrodoméstico eliminado exitosamente
        schema:
          type: object
          properties:
            mensaje:
              type: string
              example: "Electrodoméstico eliminado exitosamente"
        404:
          description: Electrodoméstico no encontrado
          schema:
            type: object
            properties:
              mensaje:
                type: string
                example: "Electrodoméstico no encontrado"
        500:
          description: Error interno del servidor
          schema:
            type: object
            properties:
              mensaje:
                type: string
                example: "Error en el servidor"
    """
    try:
        result = ElectrodomesticosService.delete_electrodomestico(electrodomestico_id)
        if not result:
            return jsonify({"mensaje": "Electrodoméstico no encontrado"}), 404

        return jsonify({"mensaje": "Electrodoméstico eliminado exitosamente"}), 200
    except Exception as e:
        logger.error(f'Error al eliminar el electrodoméstico: {str(e)}')
        return jsonify({"mensaje": "Error en el servidor"}), 500

