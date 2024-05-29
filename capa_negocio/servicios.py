# capa_negocio/servicios.py
from capa_datos import repositorios

def crear_usuario(nombre, correo):
    repositorios.agregar_usuario(nombre, correo)

def crear_bicicleta(modelo):
    repositorios.agregar_bicicleta(modelo)

def alquilar_bicicleta(usuario_id, bicicleta_id):
    return repositorios.alquilar_bicicleta(usuario_id, bicicleta_id)

def devolver_bicicleta(alquiler_id):
    return repositorios.devolver_bicicleta(alquiler_id)
