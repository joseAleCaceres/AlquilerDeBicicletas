# capa_datos/repositorios.py
from .base_datos import instancia_bd
from .modelos import Usuario, Bicicleta, Alquiler

sesion = instancia_bd.obtener_sesion()

def agregar_usuario(nombre, correo):
    usuario = Usuario(nombre=nombre, correo=correo)
    sesion.add(usuario)
    sesion.commit()

def agregar_bicicleta(modelo):
    bicicleta = Bicicleta(modelo=modelo)
    sesion.add(bicicleta)
    sesion.commit()

def alquilar_bicicleta(usuario_id, bicicleta_id):
    bicicleta = sesion.query(Bicicleta).filter_by(id=bicicleta_id, disponible=True).first()
    if bicicleta:
        alquiler = Alquiler(usuario_id=usuario_id, bicicleta_id=bicicleta_id)
        bicicleta.disponible = False
        sesion.add(alquiler)
        sesion.commit()
        return alquiler
    return None

def devolver_bicicleta(alquiler_id):
    alquiler = sesion.query(Alquiler).filter_by(id=alquiler_id, devuelto=False).first()
    if alquiler:
        alquiler.devuelto = True
        alquiler.bicicleta.disponible = True
        sesion.commit()
