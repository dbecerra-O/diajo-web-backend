from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.future import select
from config.db import get_session
from schemas.characteristic import Characteristic as CharacteristicSchema
from models.models import Characteristic as CharacteristicModel
from sqlalchemy.orm import Session

characteristic = APIRouter()

@characteristic.get("/diajosac/api/characteristics/{idProduct}", response_model=list[CharacteristicSchema])
async def get_characteristics(idProduct: int, session: Session = Depends(get_session)):
    """
    Endpoint para obtener características asociadas a un producto específico.

    Args:
        idProduct (int): El ID del producto para el cual se obtienen las características.

    Returns:
        List[Characteristic]: Una lista de objetos Characteristic asociados al producto.

    Raises:
        HTTPException: Si no se encuentran características para el producto especificado.
    """
    query = select(CharacteristicModel).where(CharacteristicModel.idProduct == idProduct)
    result = session.execute(query)
    characteristics_list = result.scalars().all()

    if not characteristics_list:
        raise HTTPException(status_code=404, detail="Characteristics not found for the specified product")

    return characteristics_list