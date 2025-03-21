from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.categories import category
from routes.products import product
from routes.brands import brand
from routes.forms import form
from routes.guias import guia

# Use venv: python -m venv venv
# Activate venv: .\venv\Scripts\activate
# install dependencies:
# pip install -r .\requirements.txt
# Comando to execute the API: uvicorn main:app --reload
# Test API: 
# Swagger UI: http://127.0.0.1:8000/docs
# ReDoc: http://127.0.0.1:8000/redoc
# ----------------------
# Use Dockerfile: docker build -t diajosac-api .
# Run the container: docker run -p 8000:8000 --name diajo-container --env-file .env diajosac-api
# Test API: 
# Swagger UI: http://localhost:8000/docs
# ReDoc: http://localhost:8000/redoc

app = FastAPI(
    title="DIAJOSAC API",
    description="API para la gestión de productos, categorías, marcas, características, formularios y colores.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(category)
app.include_router(product)
app.include_router(brand)
app.include_router(form)
app.include_router(guia)