from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    idCategory = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    image = Column(String(255), nullable=False)

class Brand(Base):
    __tablename__ = 'brands'
    idBrand = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    image = Column(String(255), nullable=False)

class ProductModel(Base):
    __tablename__ = 'products'
    idProduct = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    technical_sheet = Column(String(255), nullable=False)
    image = Column(String(255), nullable=False)
    idCategory = Column(Integer, ForeignKey('categories.idCategory'), nullable=False)
    idBrand = Column(Integer, ForeignKey('brands.idBrand'), nullable=False)

class Characteristic(Base):
    __tablename__ = 'characteristics'
    idCharacteristic = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    idProduct = Column(Integer, ForeignKey('products.idProduct'), nullable=False)

class Form(Base):
    __tablename__ = 'forms'
    idForm = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)

class Color(Base):
    __tablename__ = 'colors'
    idColor = Column(Integer, primary_key=True, index=True)
    color_name = Column(String(255), nullable=False)
    image = Column(String(255), nullable=False)
    idProduct = Column(Integer, ForeignKey('products.idProduct'), nullable=False)