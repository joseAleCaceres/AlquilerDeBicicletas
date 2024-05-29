# capa_datos/base_datos.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class BaseDatos:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.engine = create_engine('sqlite:///alquiler_bicicletas.db')
            cls._instancia.Session = sessionmaker(bind=cls._instancia.engine)
        return cls._instancia

    def obtener_sesion(self):
        return self._instancia.Session()

# Singleton: Aseguramos que solo exista una instancia de la base de datos.
instancia_bd = BaseDatos()
