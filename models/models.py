from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Text
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
              Column("number", Integer),
              Column("Description", Text))
