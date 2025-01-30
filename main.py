from fastapi import FastAPI
from routes.categories import category

# Comando to execute the API: uvicorn main:app --reload
app = FastAPI()

app.include_router(category)