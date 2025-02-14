from fastapi import APIRouter, HTTPException
from sqlalchemy.future import select
from config.db import conn
from models.models import characteristics
from schemas.characteristic import Characteristic

characteristic = APIRouter()

@characteristic.get("/diajosac/api/characteristics/{idProduct}", response_model=list[Characteristic])
async def get_characteristics(idProduct: int):
    """
    Endpoint para obtener características asociadas a un producto específico.

    Args:
        idProduct (int): El ID del producto para el cual se obtienen las características.

    Returns:
        List[Characteristic]: Una lista de objetos Characteristic asociados al producto.

    Raises:
        HTTPException: Si no se encuentran características para el producto especificado.
    """
    query = select(characteristics).where(characteristics.c.idProduct == idProduct)
    result = await conn.execute(query)
    characteristics_list = result.fetchall()

    if not characteristics_list:
        raise HTTPException(status_code=404, detail="Characteristics not found for the specified product")

    return [
        {
            "idCharacteristic": row.idCharacteristic,
            "name": row.name,
            "idProduct": row.idProduct
        }
        for row in characteristics_list
    ]