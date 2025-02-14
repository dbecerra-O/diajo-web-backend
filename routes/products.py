from fastapi import APIRouter, HTTPException, Query
from sqlalchemy.future import select
from config.db import conn
from schemas.product import Product
from models.models import products

product = APIRouter()

def result_to_dict(result):
    """
    Convierte el resultado de una consulta en una lista de diccionarios.

    Args:
        result: El resultado de la consulta.

    Returns:
        List[dict]: Una lista de diccionarios representando los productos.
    """
    return [
        {
            "idProduct": row.idProduct,
            "name": row.name,
            "description": row.description,
            "technical_sheet": row.technical_sheet,
            "image": row.image,
            "idCategory": row.idCategory,
            "idBrand": row.idBrand
        }
        for row in result
    ]

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
    query = select(products)

    if brand is not None:
        query = query.where(products.c.idBrand == brand)

    if category is not None:
        query = query.where(products.c.idCategory == category)

    if name:
        query = query.where(products.c.name.ilike(f"%{name}%"))

    result = await conn.execute(query)
    products_list = result.fetchall()

    if not products_list:
        raise HTTPException(status_code=404, detail="No se encontraron productos con esos filtros.")

    return result_to_dict(products_list)

@product.get("/diajosac/api/products/{idProduct}", response_model=Product)
async def get_product(idProduct: int):
    """
    Endpoint para obtener un producto por su ID.
    """
    query = select(products).where(products.c.idProduct == idProduct)
    result = await conn.execute(query)
    product_row = result.fetchone()

    if product_row is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return result_to_dict([product_row])[0]

@product.get("/diajosac/api/products/brand/{idBrand}", response_model=list[Product])
async def get_products_by_brand(idBrand: int):
    """
    Endpoint para obtener productos por ID de marca.
    """
    query = select(products).where(products.c.idBrand == idBrand)
    result = await conn.execute(query)
    products_list = result.fetchall()

    if not products_list:
        raise HTTPException(status_code=404, detail="Products not found")

    return result_to_dict(products_list)

@product.get("/diajosac/api/products/category/{idCategory}", response_model=list[Product])
async def get_products_by_category(idCategory: int):
    """
    Endpoint para obtener productos por ID de categoría.
    """
    query = select(products).where(products.c.idCategory == idCategory)
    result = await conn.execute(query)
    products_list = result.fetchall()

    if not products_list:
        raise HTTPException(status_code=404, detail="Products not found")

    return result_to_dict(products_list)

@product.get("/diajosac/api/products/brand/{idBrand}/category/{idCategory}", response_model=list[Product])
async def get_products_by_brand_and_category(idBrand: int, idCategory: int):
    """
    Endpoint para obtener productos por ID de marca y categoría.
    """
    query = select(products).where(products.c.idBrand == idBrand, products.c.idCategory == idCategory)
    result = await conn.execute(query)
    products_list = result.fetchall()

    if not products_list:
        raise HTTPException(status_code=404, detail="Products not found")

    return result_to_dict(products_list)