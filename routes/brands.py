from fastapi import APIRouter, HTTPException
from models.models import brands
from config.db import conn

brand = APIRouter()

@brand.get("/diajosac/api/brands")
async def get_brands():
    query = brands.select()
    result = conn.execute(query).fetchall()

    brands_list = []
    for row in result:
        brand_dict = {
            "idBrand": row[0],
            "name": row[1],
            "image": row[2]
        }
        brands_list.append(brand_dict)

    return {"brands": brands_list}

@brand.get("/diajosac/api/brands/{idBrand}")
async def get_brand(idBrand: int):
    query = brands.select().where(brands.c.idBrand == idBrand)
    result = conn.execute(query).fetchone()

    if result is None:
        raise HTTPException(status_code=404, detail="Brand not found")

    brand_dict = {
        "idBrand": result[0],
        "name": result[1],
        "image": result[2]
    }

    return {"brand": brand_dict}