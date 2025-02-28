from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.future import select
from config.db import get_session
from schemas.category import Category
from models.models import Category as CategoryModel
from sqlalchemy.orm import Session

category = APIRouter()

@category.get("/diajosac/api/categories", response_model=list[Category])
async def get_categories(session: Session = Depends(get_session)):
    """
    Obtiene una lista de todas las categorías.

    Returns:
        List[Category]: Una lista de objetos Category.

    Raises:
        HTTPException: Si no se encuentran categorías.
    """
    query = select(CategoryModel)
    result = session.execute(query)
    categories_list = result.scalars().all()

    if not categories_list:
        raise HTTPException(status_code=404, detail="Categories not found")

    return categories_list

@category.get("/diajosac/api/categories/{idCategory}", response_model=Category)
async def get_category(idCategory: int, session: Session = Depends(get_session)):
    """
    Endpoint para obtener una categoría por su ID.
    """
    query = select(CategoryModel).where(CategoryModel.id == idCategory)
    result = session.execute(query)
    category_row = result.scalars().first()

    if category_row is None:
        raise HTTPException(status_code=404, detail="Category not found")

    return category_row