# capa_negocio/cadena_alquiler.py
from capa_datos import repositorios

class ManejadorAlquiler:
    def establecer_siguiente(self, manejador):
        self.siguiente_manejador = manejador
        return manejador

    def manejar(self, solicitud):
        if self.siguiente_manejador:
            return self.siguiente_manejador.manejar(solicitud)
        return None

class ManejadorVerificarUsuario(ManejadorAlquiler):
    def manejar(self, solicitud):
        usuario = repositorios.sesion.query(repositorios.Usuario).filter_by(id=solicitud['usuario_id']).first()
        if usuario:
            return super().manejar(solicitud)
        return "Usuario no encontrado."

class ManejadorVerificarDisponibilidadBicicleta(ManejadorAlquiler):
    def manejar(self, solicitud):
        bicicleta = repositorios.sesion.query(repositorios.Bicicleta).filter_by(id=solicitud['bicicleta_id'], disponible=True).first()
        if bicicleta:
            return super().manejar(solicitud)
        return "Bicicleta no disponible."

class ManejadorProcesarAlquiler(ManejadorAlquiler):
    def manejar(self, solicitud):
        alquiler = repositorios.alquilar_bicicleta(solicitud['usuario_id'], solicitud['bicicleta_id'])
        if alquiler:
            return "Alquiler procesado exitosamente."
        return "Fallo en el procesamiento del alquiler."

# Uso de la cadena de responsabilidad para procesar un alquiler
def procesar_alquiler(usuario_id, bicicleta_id):
    verificar_usuario = ManejadorVerificarUsuario()
    verificar_bicicleta = ManejadorVerificarDisponibilidadBicicleta()
    procesar_alquiler = ManejadorProcesarAlquiler()

    verificar_usuario.establecer_siguiente(verificar_bicicleta).establecer_siguiente(procesar_alquiler)

    return verificar_usuario.manejar({'usuario_id': usuario_id, 'bicicleta_id': bicicleta_id})
