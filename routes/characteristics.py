from fastapi import APIRouter, HTTPException
from models.models import characteristics
from config.db import conn
from schemas.characteristic import Characteristic

characteristic = APIRouter()

@characteristic.get("/diajosac/api/characteristics/{idProduct}", response_model=list[Characteristic])
async def get_characteristics(idProduct: int):
    query = characteristics.select().where(characteristics.c.idProduct == idProduct)
    result = conn.execute(query).fetchall()

    if result is None:
        raise HTTPException(status_code=404, detail="Characteristics not found")

    characteristics_list = []
    for row in result:
        characteristic_dict = {
            "idCharacteristic": row[0],
            "name": row[1],
            "value": row[2]
        }
        characteristics_list.append(characteristic_dict)

    return characteristics_list