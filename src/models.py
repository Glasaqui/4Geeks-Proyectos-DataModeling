import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table usuario
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    adress1 = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(10), nullable=False)

class FavoritosPer(Base):
    __tablename__ = 'favoritosperson'
    # Here we define columns for the table favoritos.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    personaje_id = Column(Integer, ForeignKey("personajes.id"))
       
class FavoritosPla(Base):
    __tablename__ = 'favoritosplanet'
    # Here we define columns for the table favoritos.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    planeta_id = Column(Integer, ForeignKey("planetas.id"))
    
class Planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table favoritos.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gravedad = Column(String(250), nullable=False)

class Personajes(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table favoritos.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    clasificacion = Column(String(250), nullable=False)
    lenguaje = Column(String(250), nullable=False)
    creacion = Column(String(250), nullable=False)
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')