from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import Integer, String, Text, DateTime
from config.db import meta, engine

# Modelo de Categorias
categories = Table("categories", meta, 
              Column("idCategory", Integer, primary_key=True), 
              Column("name", String(255)),
              Column("image", String(255)))

# Modelo de Marcas
brands = Table("brands", meta, 
               Column("idBrand", Integer, primary_key=True), 
               Column("name", String(255)),
               Column("image", String(255)))  # URL de la imagen

# Modelo de Productos
products = Table("products", meta, 
                 Column("idProduct", Integer, primary_key=True), 
                 Column("name", String(255)),
                 Column("description", Text),
                 Column("technical_sheet", String(255)), # URL de la hoja técnica
                 Column("image", String(255)),  # URL de la imagen
                 Column("idCategory", Integer, ForeignKey("categories.idCategory")),
                 Column("idBrand", Integer, ForeignKey("brands.idBrand")))

# Modelo de Caracteristicas
characteristics = Table("characteristics", meta, 
                        Column("idCharacteristic", Integer, primary_key=True), 
                        Column("name", String(255)),
                        Column("idProduct", Integer, ForeignKey("products.idProduct")))

# Modelo de Formularios
forms = Table("forms", meta, 
              Column("idForm", Integer, primary_key=True), 
              Column("name", String(255)),
              Column("last_name", String(255)),
              Column("email", String(255)),
              Column("phone", Integer),
              Column("description", Text),
              Column("created_at", DateTime, default=func.now()))

# Modelo de Colores
colors = Table("colors", meta, 
               Column("idColor", Integer, primary_key=True),
               Column("color_name", String(255)),
               Column("image", String(255)))

# Modelo de Relación entre Productos y Colores
product_colors = Table("product_colors", meta,
                       Column("idProduct", Integer, ForeignKey("products.idProduct"), primary_key=True),
                       Column("idColor", Integer, ForeignKey("colors.idColor"), primary_key=True))