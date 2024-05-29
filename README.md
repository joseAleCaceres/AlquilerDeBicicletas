# AlquilerDeBicicletas
## Instrucciones para Instalar Python y Ejecutar el Proyecto

### Instalación de Python

### Windows

#### Paso 1: Descargar el Instalador de Python

1. Ve a la página oficial de descargas de Python: (https://www.python.org/downloads/)
2. Descarga la última versión de Python para Windows.

#### Paso 2: Instalar Python

1. Ejecuta el instalador descargado.
2. Asegúrate de seleccionar la opción **"Add Python to PATH"**.
3. Haz clic en **"Install Now"**.
4. Espera a que se complete la instalación.

### Ejecutar el Proyecto

#### Paso1: Descargar Dependencias

1. Abre una terminal en el directorio del proyecto
2. Ejecuta el siguiente comando para instalar sqlalchemy:

pip install sqlalchemy

#### Paso1: Descargar Dependencias
1. Abre una terminal en el directorio del proyecto
2. Ejecuta el siguiente comando:

python principal.py

## Resumen de cumplimiento de SOLID, patrones de diseño y arquitectura.

### Principios Solid

- SRP (Principio de Responsabilidad Única): Se aplica en los servicios de negocio, donde cada clase se encarga de una sola tarea.

- OCP (Principio de Abierto/Cerrado): Utilizado mediante el patrón decorador para extender el comportamiento de los servicios sin modificar su código base.

- LSP (Principio de Sustitución de Liskov): Las subclases de modelos son intercambiables sin afectar la funcionalidad del sistema.

- ISP (Principio de Segregación de la Interfaz): La arquitectura en capas asegura que las interfaces sean independientes entre sí.

- DIP (Principio de Inversión de Dependencias): Implementado mediante la inyección de dependencias para que las capas de alto nivel dependan de abstracciones en lugar de implementaciones concretas.

### Patrones de diseño

- Patrón Singleton: Se implementa en base_datos.py para garantizar que solo exista una instancia de esta.
- Patrón Cadena de Responsabilidad: Se utiliza en servicios.py para encadenar operaciones relacionadas.
- Patrón Decorador: Se aplica en decoradores.py para extender el comportamiento de los servicios de negocio sin modificar su código base.

### Arquitectura de tres capas

- Capa de acceso a datos: capa_datos
- Capa de negocio: capa_negocio
- Capa de presentación: capa_presentacion
