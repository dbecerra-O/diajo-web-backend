from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.future import select
from config.db import get_session
from schemas.brand import Brand as BrandSchema
from models.models import Brand as BrandModel
from sqlalchemy.orm import Session

brand = APIRouter()

@brand.get("/diajosac/api/brands", response_model=list[BrandSchema])
async def get_brands(session: Session = Depends(get_session)):
    """
    Obtiene una lista de todas las marcas.

    Returns:
        List[Brand]: Una lista de objetos Brand.

    Raises:
        HTTPException: Si no se encuentran marcas.
    """
    query = select(BrandModel)
    result = session.execute(query)
    brands_list = result.scalars().all()

    if not brands_list:
        raise HTTPException(status_code=404, detail="Brands not found")

    return brands_list

@brand.get("/diajosac/api/brands/{idBrand}", response_model=BrandSchema)
async def get_brand(idBrand: int, session: Session = Depends(get_session)):
    """
    Endpoint para obtener una marca por su ID.
    """
    query = select(BrandModel).where(BrandModel.id == idBrand)
    result = session.execute(query)
    brand_row = result.scalars().first()

    if brand_row is None:
        raise HTTPException(status_code=404, detail="Brand not found")

    return brand_row