import json

def generar_informe_ventas():
    with open('data/ventas.json', 'r') as file:
        ventas = [json.loads(line) for line in file]
    
    for venta in ventas:
        print(f"Fecha: {venta['fecha']}")
        print(f"Cliente: {venta['cliente']['nombre']} - {venta['cliente']['direccion']}")
        print(f"Empleado: {venta['empleado']['nombre']} - {venta['empleado']['cargo']}")
        for producto in venta['productos']:
            print(f"Producto: {producto['nombre']} - Cantidad: {producto['cantidad']} - Precio: {producto['precio']}")
        print("----------")

def generar_informe_stock(productos):
    print("Informe de Stock:")
    for categoria, items in productos.items():
        print(f"\n{categoria}:")
        for producto, cantidad in items.items():
            print(f"{producto}: {cantidad} unidades")