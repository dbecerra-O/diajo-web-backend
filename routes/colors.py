from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.future import select
from config.db import get_session
from schemas.color import Color as ColorSchema
from models.models import Color as ColorModel
from sqlalchemy.orm import Session

color = APIRouter()

@color.get("/diajosac/api/colors/{idProduct}", response_model=list[ColorSchema])
async def get_colors(idProduct: int, session: Session = Depends(get_session)):
    """
    Obtiene una lista de colores asociados a un producto específico.

    Args:
        idProduct (int): El ID del producto para el cual se obtienen los colores.

    Returns:
        List[Color]: Una lista de objetos Color asociados al producto.

    Raises:
        HTTPException: Si no se encuentran colores para el producto especificado.
    """
    query = select(ColorModel).where(ColorModel.idProduct == idProduct)
    result = session.execute(query)
    colors_list = result.scalars().all()

    if not colors_list:
        raise HTTPException(status_code=404, detail="Colors not found for the specified product")

    return colors_list