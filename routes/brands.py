from fastapi import APIRouter, HTTPException
from sqlalchemy.future import select
from models.models import brands
from config.db import conn
from schemas.brand import Brand

brand = APIRouter()

@brand.get("/diajosac/api/brands", response_model=list[Brand])
async def get_brands():
    """
    Obtiene una lista de todas las marcas.

    Returns:
        List[Brand]: Una lista de objetos Brand.

    Raises:
        HTTPException: Si no se encuentran marcas.
    """
    query = select(brands)
    result = conn.execute(query)
    brands_list = result.fetchall()

    if not brands_list:
        raise HTTPException(status_code=404, detail="Brands not found")

    return [
        {
            "idBrand": row.idBrand,
            "name": row.name,
            "image": row.image
        }
        for row in brands_list
    ]

@brand.get("/diajosac/api/brands/{idBrand}", response_model=Brand)
async def get_brand(idBrand: int):
    """
    Obtiene una marca específica por su ID.

    Args:
        idBrand (int): El ID de la marca a obtener.

    Returns:
        Brand: Un objeto Brand.

    Raises:
        HTTPException: Si no se encuentra la marca.
    """
    query = select(brands).where(brands.c.idBrand == idBrand)
    result = await conn.execute(query)
    brand_row = result.fetchone()

    if brand_row is None:
        raise HTTPException(status_code=404, detail="Brand not found")

    return {
        "idBrand": brand_row.idBrand,
        "name": brand_row.name,
        "image": brand_row.image
    }