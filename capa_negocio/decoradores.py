# capa_negocio/decoradores.py
import functools

def decorador_log(func):
    @functools.wraps(func)
    def envoltura(*args, **kwargs):
        resultado = func(*args, **kwargs)
        print(f"Función {func.__name__} llamada con args {args}, kwargs {kwargs} - Resultado: {resultado}")
        return resultado
    return envoltura
