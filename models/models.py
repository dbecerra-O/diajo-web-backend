from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import Integer, String, Text, DateTime
from config.db import meta, engine

# Modelo de Categorias
categories = Table("categories", meta, 
              Column("idCategory", Integer, primary_key=True), 
              Column("name", String(255), nullable=False),
              Column("image", String(255), nullable=False))

# Modelo de Marcas
brands = Table("brands", meta, 
               Column("idBrand", Integer, primary_key=True), 
               Column("name", String(255), nullable=False),
               Column("image", String(255), nullable=False))  # URL de la imagen

# Modelo de Productos
products = Table("products", meta, 
                 Column("idProduct", Integer, primary_key=True), 
                 Column("name", String(255), nullable=False),
                 Column("description", Text, nullable=False),
                 Column("technical_sheet", String(255), nullable=False), # URL de la hoja técnica
                 Column("image", String(255), nullable=False),  # URL de la imagen
                 Column("idCategory", Integer, ForeignKey("categories.idCategory"), nullable=False),
                 Column("idBrand", Integer, ForeignKey("brands.idBrand"), nullable=False))

# Modelo de Caracteristicas
characteristics = Table("characteristics", meta, 
                        Column("idCharacteristic", Integer, primary_key=True), 
                        Column("name", String(255), nullable=False),
                        Column("idProduct", Integer, ForeignKey("products.idProduct"), nullable=False))

# Modelo de Formularios
forms = Table("forms", meta, 
              Column("idForm", Integer, primary_key=True), 
              Column("name", String(255), nullable=False),
              Column("last_name", String(255), nullable=False),
              Column("email", String(255), nullable=False),
              Column("phone", String(20), nullable=False),
              Column("description", Text, nullable=False),
              Column("created_at", DateTime, default=func.now(), nullable=False))

# Modelo de Colores
colors = Table("colors", meta, 
               Column("idColor", Integer, primary_key=True),
               Column("color_name", String(255), nullable=False),
               Column("image", String(255), nullable=False),
               Column("idProduct", Integer, ForeignKey("products.idProduct"), nullable=False))

# Crear todas las tablas en la base de datos
meta.create_all(engine)