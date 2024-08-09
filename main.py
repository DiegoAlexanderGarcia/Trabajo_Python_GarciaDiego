import json
from ventas import registrar_venta
from compras import registrar_compra
from informes import generar_informe_ventas, generar_informe_stock

def cargar_datos(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def guardar_datos(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


productos = cargar_datos('data/productos.json')
print("Bienvenido a PanCamp - Sistema de Gestión")
while True:
    print("\n1. Registrar Venta")
    print("2. Registrar Compra")
    print("3. Generar Informe de Ventas")
    print("4. Generar Informe de Stock")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        registrar_venta(productos)
    elif opcion == '2':
        registrar_compra(productos)
    elif opcion == '3':
        generar_informe_ventas()
    elif opcion == '4':
        generar_informe_stock(productos)
    elif opcion == '5':
        guardar_datos('data/productos.json', productos)
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida, intente nuevamente.")


