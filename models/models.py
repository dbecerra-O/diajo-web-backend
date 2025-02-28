from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    image = Column(String(255), nullable=False)

class Brand(Base):
    __tablename__ = 'brands'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    image = Column(String(255), nullable=False)

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    technical_sheet = Column(String(255), nullable=False)
    image = Column(String(255), nullable=False)
    idCategory = Column(Integer, ForeignKey('categories.id'), nullable=False)
    idBrand = Column(Integer, ForeignKey('brands.id'), nullable=False)

    # Relación con colores y características
    colors = relationship("Color", backref="product", lazy="selectin")
    characteristics = relationship("Characteristic", backref="product", lazy="selectin")

class Characteristic(Base):
    __tablename__ = 'characteristics'
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(255), nullable=False)
    idProduct = Column(Integer, ForeignKey('products.id'), nullable=False)

class Form(Base):
    __tablename__ = 'forms'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)

class Color(Base):
    __tablename__ = 'colors'
    id = Column(Integer, primary_key=True, index=True)
    color_name = Column(String(255), nullable=False)
    image = Column(String(255), nullable=False)
    idProduct = Column(Integer, ForeignKey('products.id'), nullable=False)

class Guia(Base):
    __tablename__ = 'guias'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    archive = Column(String(255), nullable=False)