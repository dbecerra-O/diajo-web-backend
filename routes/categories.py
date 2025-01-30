from sqlalchemy import select
from fastapi import APIRouter, HTTPException
from models.models import categories
from config.db import conn
import base64

category = APIRouter()

@category.get("/categories")
async def get_categories():
    query = categories.select()
    result = conn.execute(query).fetchall() 
    
    categories_list = []
    for row in result:
        category_dict = {
            "idCategory": row[0],
            "name": row[1],
            "image": row[2]
        }
        categories_list.append(category_dict)
    
    return {"categories": categories_list}

@category.get("/categories/{idCategory}")
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
    
    return {"category": category_dict}