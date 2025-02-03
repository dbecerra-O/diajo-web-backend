from fastapi import APIRouter, HTTPException
from models.models import categories
from config.db import conn
from schemas.category import Category

category = APIRouter()

@category.get("/diajosac/api/categories", response_model=list[Category])
async def get_categories():
    query = categories.select()
    result = conn.execute(query).fetchall()
    
    if result is None:
        raise HTTPException(status_code=404, detail="Categories not found")
    
    categories_list = []
    for row in result:
        category_dict = {
            "idCategory": row[0],
            "name": row[1],
            "image": row[2]
        }
        categories_list.append(category_dict)
    
    return categories_list

@category.get("/diajosac/api/categories/{idCategory}", response_model=Category)
async def get_category(idCategory: int):
    query = categories.select().where(categories.c.idCategory == idCategory)
    result = conn.execute(query).fetchone()
    
    if result is None:
        raise HTTPException(status_code=404, detail="Category not found")
    
    category_dict = {
        "idCategory": result[0],
        "name": result[1],
        "image": result[2]
    }
    
    return category_dict