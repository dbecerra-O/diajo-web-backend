from fastapi import APIRouter, HTTPException, Query, Depends
from sqlalchemy.future import select
from fastapi_pagination import Page, add_pagination, Params
from fastapi_pagination.ext.sqlalchemy import paginate
from config.db import get_session
from typing import List, Optional
from schemas.product import Product
from models.models import ProductModel
from sqlalchemy.orm import Session
from config.exceptions import ProductNotFoundException

product = APIRouter()
add_pagination(product)

@product.get("/diajosac/api/products", response_model=Page[Product])
async def get_products(
    brand: Optional[List[int]] = Query(None, alias="idBrand"),
    category: Optional[List[int]] = Query(None, alias="idCategory"),
    name: Optional[str] = Query(None, min_length=3),  # Establecer un valor predeterminado para el tamaño de la página
    params: Params = Depends(),
    session: Session = Depends(get_session)
):
    """
    Endpoint para obtener productos con filtros opcionales:
    - brand: Filtra por la marca (idBrand).
    - category: Filtra por la categoría (idCategory).
    - name: Filtra por el nombre del producto (busca parcialmente).
    """
    query = select(ProductModel)

    if brand:
        query = query.where(ProductModel.idBrand.in_(brand))

    if category:
        query = query.where(ProductModel.idCategory.in_(category))

    if name:
        query = query.where(ProductModel.name.ilike(f"%{name}%"))

    # Ejecutar la consulta y obtener los resultados
    result = session.execute(query)
    products = result.scalars().all()

    # Si no se encuentran productos, lanzar la excepción personalizada
    if not products:
        raise ProductNotFoundException()
    
    # Usa paginate para paginar tu consulta
    return paginate(session, query, params)

@product.get("/diajosac/api/products/{idProduct}", response_model=Product)
async def get_product(idProduct: int, session: Session = Depends(get_session)):
    """
    Endpoint para obtener un producto por su ID.
    """
    query = select(ProductModel).where(ProductModel.idProduct == idProduct)
    result = session.execute(query)
    product_row = result.scalars().first()

    if product_row is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return product_row