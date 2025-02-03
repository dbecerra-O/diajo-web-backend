from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.categories import category
from routes.products import product
from routes.brands import brand
from routes.characteristics import characteristic
from routes.forms import form

# Comando to execute the API: uvicorn main:app --reload
# ----------------------
# install dependencies:
# pip install -r .\requirements.txt

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(category)
app.include_router(product)
app.include_router(brand)
app.include_router(characteristic)
app.include_router(form)