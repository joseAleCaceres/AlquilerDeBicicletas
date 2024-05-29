# capa_datos/modelos.py
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .base_datos import Base

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    correo = Column(String, unique=True)

class Bicicleta(Base):
    __tablename__ = 'bicicletas'
    id = Column(Integer, primary_key=True)
    modelo = Column(String)
    disponible = Column(Boolean, default=True)

class Alquiler(Base):
    __tablename__ = 'alquileres'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    bicicleta_id = Column(Integer, ForeignKey('bicicletas.id'))
    devuelto = Column(Boolean, default=False)

    usuario = relationship("Usuario")
    bicicleta = relationship("Bicicleta")
