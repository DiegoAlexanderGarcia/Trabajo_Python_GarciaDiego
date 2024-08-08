# PanCamp - Trabajo_Python_GarciaDiego

Este proyecto es un sistema básico para gestionar registros de compras y ventas en una panadería. Los datos se almacenan en un archivo JSON y se pueden registrar detalles de cada venta, incluyendo información sobre el cliente, el empleado que realizó la venta, y los productos vendidos.

## Características

- **Registro de Ventas**: Permite ingresar información sobre cada venta, incluyendo:
  - Fecha de la venta.
  - Información del cliente (nombre, dirección).
  - Información del empleado que realizó la venta (nombre, cargo).
  - Detalles de los productos vendidos (nombre, cantidad, precio).

- **Almacenamiento de Datos**: Los registros de ventas se almacenan en un archivo JSON (`reg_comprasVentas.json`), lo que permite que los datos persistan entre ejecuciones del programa.

## Requisitos

- Python 3.6 o superior

## Instrucciones de Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/tu_usuario/ProyectoPanCamp.git
   cd ProyectoPanCamp
