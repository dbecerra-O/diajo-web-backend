# routes/colors.py
from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from config.db import conn
from schemas.color import Color  # El esquema para colores
from models.models import colors, product_colors  # Modelos relacionados con colores

color = APIRouter()

@color.get("/diajosac/api/products/{idProduct}/colors", response_model=list[Color])
async def get_product_colors(idProduct: int):
    query = select([colors.c.idColor, colors.c.color_name, colors.c.image]).\
        join(product_colors, product_colors.c.idColor == colors.c.idColor).\
        where(product_colors.c.idProduct == idProduct)

    result = conn.execute(query).fetchall()

    if not result:
        raise HTTPException(status_code=404, detail="No se encontraron colores para este producto.")

    colors_list = [{"idColor": row[0], "color_name": row[1], "image": row[2]} for row in result]

    return colors_list