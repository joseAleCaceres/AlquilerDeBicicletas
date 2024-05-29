# capa_presentacion/inicio.py
import capa_negocio.servicios as servicios
import capa_negocio.cadena_alquiler as cadena_alquiler
from capa_negocio.decoradores import decorador_log

@decorador_log
def menu_principal():
    while True:
        print("\nSistema de Alquiler de Bicicletas de Montaña")
        print("1. Registrar Usuario")
        print("2. Registrar Bicicleta")
        print("3. Alquilar Bicicleta")
        print("4. Devolver Bicicleta")
        print("5. Salir")

        eleccion = input("Elige una opción: ")

        if eleccion == '1':
            nombre = input("Nombre del usuario: ")
            correo = input("Correo del usuario: ")
            servicios.crear_usuario(nombre, correo)
            print("Usuario registrado exitosamente!")
        
        elif eleccion == '2':
            modelo = input("Modelo de la bicicleta: ")
            servicios.crear_bicicleta(modelo)
            print("Bicicleta registrada exitosamente!")

        elif eleccion == '3':
            usuario_id = input("ID del usuario: ")
            bicicleta_id = input("ID de la bicicleta: ")
            resultado = cadena_alquiler.procesar_alquiler(int(usuario_id), int(bicicleta_id))
            print(resultado)

        elif eleccion == '4':
            alquiler_id = input("ID del alquiler: ")
            servicios.devolver_bicicleta(int(alquiler_id))
            print("Bicicleta devuelta exitosamente!")

        elif eleccion == '5':
            print("Saliendo de la aplicación.")
            break

        else:
            print("Elección inválida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    menu_principal()
