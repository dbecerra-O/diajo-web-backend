from fastapi import APIRouter, HTTPException, Query
from models.models import products
from config.db import conn
from schemas.product import Product

product = APIRouter()

@product.get("/diajosac/api/products", response_model=list[Product])
async def get_products(
    brand: int = Query(None, alias="idBrand"), 
    category: int = Query(None, alias="idCategory"),
    name: str = Query(None, min_length=3)
):
    """
    Endpoint para obtener productos con filtros opcionales:
    - brand: Filtra por la marca (idBrand).
    - category: Filtra por la categoría (idCategory).
    - name: Filtra por el nombre del producto (busca parcialmente).
    """
    query = products.select()
    
    if brand is not None:
        query = query.where(products.c.idBrand == brand)
    
    if category is not None:
        query = query.where(products.c.idCategory == category)
    
    if name:
        query = query.where(products.c.name.ilike(f"%{name}%"))
    
    result = conn.execute(query).fetchall()
    
    if not result:
        raise HTTPException(status_code=404, detail="No se encontraron productos con esos filtros.")
    
    products_list = []
    for row in result:
        product_dict = {
            "idProduct": row[0],
            "name": row[1],
            "description": row[2],
            "technical_sheet": row[3],
            "image": row[4],
            "idCategory": row[5],
            "idBrand": row[6]
        }
        products_list.append(product_dict)
    
    return products_list
            
@product.get("/diajosac/api/products/{idProduct}", response_model=Product)
async def get_product(idProduct: int):
    query = products.select().where(products.c.idProduct == idProduct)
    result = conn.execute(query).fetchone()
    
    if result is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    product_dict = {
        "idProduct": result[0],
        "name": result[1],
        "description": result[2],
        "technical_sheet": result[3],
        "image": result[4],
        "idCategory": result[5],
        "idBrand": result[6]
    }
    
    return product_dict

@product.get("/diajosac/api/products/{idBrand}", response_model=list[Product])
async def get_products_by_brand(idBrand: int):
    query = products.select().where(products.c.idBrand == idBrand)
    result = conn.execute(query).fetchall()
    
    if result is None:
        raise HTTPException(status_code=404, detail="Products not found")
    
    products_list = []
    for row in result:
        product_dict = {
            "idProduct": row[0],
            "name": row[1],
            "description": row[2],
            "technical_sheet": row[3],
            "image": row[4],
            "idCategory": row[5],
            "idBrand": row[6]
        }
        products_list.append(product_dict)
    
    return products_list

@product.get("/diajosac/api/products/{idCategory}", response_model=list[Product])
async def get_products_by_category(idCategory: int):
    query = products.select().where(products.c.idCategory == idCategory)
    result = conn.execute(query).fetchall()
    
    if result is None:
        raise HTTPException(status_code=404, detail="Products not found")
    
    products_list = []
    for row in result:
        product_dict = {
            "idProduct": row[0],
            "name": row[1],
            "description": row[2],
            "technical_sheet": row[3],
            "image": row[4],
            "idCategory": row[5],
            "idBrand": row[6]
        }
        products_list.append(product_dict)
    
    return products_list

@product.get("/diajosac/api/products/{idBrand}/{idCategory}", response_model=list[Product])
async def get_products_by_brand_and_category(idBrand: int, idCategory: int):
    query = products.select().where(products.c.idBrand == idBrand).where(products.c.idCategory == idCategory)
    result = conn.execute(query).fetchall()
    
    if result is None:
        raise HTTPException(status_code=404, detail="Products not found")
    
    products_list = []
    for row in result:
        product_dict = {
            "idProduct": row[0],
            "name": row[1],
            "description": row[2],
            "technical_sheet": row[3],
            "image": row[4],
            "idCategory": row[5],
            "idBrand": row[6]
        }
        products_list.append(product_dict)

    return products_list