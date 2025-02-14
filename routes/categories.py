from fastapi import APIRouter, HTTPException
from sqlalchemy.future import select
from models.models import categories
from config.db import conn
from schemas.category import Category

category = APIRouter()

@category.get("/diajosac/api/categories", response_model=list[Category])
async def get_categories():
    """
    Obtiene una lista de todas las categorías.

    Returns:
        List[Category]: Una lista de objetos Category.

    Raises:
        HTTPException: Si no se encuentran categorías.
    """
    query = select(categories)
    result = conn.execute(query)
    categories_list = result.fetchall()

    if not categories_list:
        raise HTTPException(status_code=404, detail="Categories not found")

    return [
        {
            "idCategory": row.idCategory,
            "name": row.name,
            "image": row.image
        }
        for row in categories_list
    ]

@category.get("/diajosac/api/categories/{idCategory}", response_model=Category)
async def get_category(idCategory: int):
    """
    Obtiene una categoría específica por su ID.

    Args:
        idCategory (int): El ID de la categoría a obtener.

    Returns:
        Category: Un objeto Category.

    Raises:
        HTTPException: Si no se encuentra la categoría.
    """
    query = select(categories).where(categories.c.idCategory == idCategory)
    result = conn.execute(query)
    category_row = result.fetchone()

    if category_row is None:
        raise HTTPException(status_code=404, detail="Category not found")

    return {
        "idCategory": category_row.idCategory,
        "name": category_row.name,
        "image": category_row.image
    }