from fastapi import APIRouter, HTTPException
from sqlalchemy.future import select
from config.db import conn
from schemas.color import Color  # El esquema para colores
from models.models import colors  # Modelos relacionados con colores

color = APIRouter()

@color.get("/diajosac/api/colors/{idProduct}", response_model=list[Color])
async def get_colors(idProduct: int):
    """
    Obtiene una lista de colores asociados a un producto específico.

    Args:
        idProduct (int): El ID del producto para el cual se obtienen los colores.

    Returns:
        List[Color]: Una lista de objetos Color asociados al producto.

    Raises:
        HTTPException: Si no se encuentran colores para el producto especificado.
    """
    query = select(colors).where(colors.c.idProduct == idProduct)
    result = conn.execute(query)
    colors_list = result.fetchall()

    if not colors_list:
        raise HTTPException(status_code=404, detail="Colors not found for the specified product")

    return [
        {
            "idColor": row.idColor,
            "color_name": row.color_name,
            "image": row.image,
            "idProduct": row.idProduct
        }
        for row in colors_list
    ]