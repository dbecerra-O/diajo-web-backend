from fastapi import FastAPI
from routes.categories import category
from routes.products import product
from routes.brands import brand
from routes.characteristics import characteristic
from routes.forms import form

# Comando to execute the API: uvicorn main:app --reload
app = FastAPI()

app.include_router(category)
app.include_router(product)
app.include_router(brand)
app.include_router(characteristic)
app.include_router(form)