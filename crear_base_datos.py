# crear_base_datos.py
from capa_datos.base_datos import Base, instancia_bd
from capa_datos.modelos import Usuario, Bicicleta, Alquiler

def crear_tablas():
    engine = instancia_bd.engine
    Base.metadata.create_all(engine)
    print("Tablas creadas exitosamente.")

if __name__ == "__main__":
    crear_tablas()
