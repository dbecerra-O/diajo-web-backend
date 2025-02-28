from fastapi import APIRouter, HTTPException, Query, Depends
from sqlalchemy.future import select
from fastapi_pagination import Page, add_pagination, Params
from fastapi_pagination.ext.sqlalchemy import paginate
from config.db import get_session
from typing import List, Optional
from schemas.product import Product, ProductSimple
from models.models import Product as ProductModel
from sqlalchemy.orm import Session, selectinload

product = APIRouter()
add_pagination(product)

@product.get("/diajosac/api/products", response_model=Page[ProductSimple])
async def get_products(
    brand: Optional[List[int]] = Query(None, alias="idBrand"),
    category: Optional[List[int]] = Query(None, alias="idCategory"),
    name: Optional[str] = Query(None, min_length=3),
    params: Params = Depends(),
    session: Session = Depends(get_session),
):
    """
    Devuelve una lista paginada de productos sin relaciones.
    """
    query = select(ProductModel)  # Ahora devuelve todos los datos del producto

    if brand:
        query = query.where(ProductModel.idBrand.in_(brand))

    if category:
        query = query.where(ProductModel.idCategory.in_(category))

    if name:
        query = query.where(ProductModel.name.ilike(f"%{name}%"))

    return paginate(session, query, params)  # Paginación


@product.get("/diajosac/api/products/{idProduct}", response_model=Product)
async def get_product(idProduct: int, session: Session = Depends(get_session)):
    """
    Devuelve un producto con todos sus datos, incluyendo colores y características.
    """
    query = (
        select(ProductModel)
        .where(ProductModel.idProduct == idProduct)
        .options(
            selectinload(ProductModel.colors),  # Cargar colores
            selectinload(ProductModel.characteristics)  # Cargar características
        )
    )
    
    result = session.execute(query)
    product_row = result.scalars().first()

    if product_row is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return product_row