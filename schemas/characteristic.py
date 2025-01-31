from pydantic import BaseModel

class CharacteristicBase(BaseModel):
    name: str
    idProduct: int

class Characteristic(CharacteristicBase):
    idCharacteristic: int

    class Config:
        orm_mode = True
