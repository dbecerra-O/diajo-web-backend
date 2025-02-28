from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.future import select
from fastapi_pagination import Page, add_pagination, Params
from fastapi_pagination.ext.sqlalchemy import paginate
from config.db import get_session
from models.models import Guia as GuiaModel
from schemas.guia import Guia
from sqlalchemy.orm import Session

guia = APIRouter()
add_pagination(guia)

@guia.get("/diajosac/api/guia", response_model=Page[Guia])
async def get_guias(
    params: Params = Depends(),
    session: Session = Depends(get_session)
):
    """
    Devuelve una lista paginada de guías sin relaciones.
    """
    query = select(GuiaModel)
    return paginate(session, query, params)

@guia.get("/diajosac/api/guia/{idGuia}", response_model=Guia)
async def get_guia(idGuia: int, session: Session = Depends(get_session)):
    """
    Devuelve un guia con todos sus datos, incluyendo colores y características.
    """
    query = select(GuiaModel).where(GuiaModel.id == idGuia)
    result = session.execute(query)
    guia_row = result.scalars().first()

    if guia_row is None:
        raise HTTPException(status_code=404, detail="Guia not found")

    return guia_row