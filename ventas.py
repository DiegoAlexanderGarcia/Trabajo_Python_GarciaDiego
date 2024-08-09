import json

def registrar_venta(productos):
    fecha = input("Ingrese la fecha de la venta (YYYY-MM-DD): ")
    nombre_cliente = input("Nombre del cliente: ")
    direccion_cliente = input("Dirección del cliente: ")
    nombre_empleado = input("Nombre del empleado: ")
    cargo_empleado = input("Cargo del empleado: ")
    
    venta = {
        "fecha": fecha,
        "cliente": {
            "nombre": nombre_cliente,
            "direccion": direccion_cliente
        },
        "empleado": {
            "nombre": nombre_empleado,
            "cargo": cargo_empleado
        },
        "productos": []
    }
    
    while True:
        producto = input("Nombre del producto (o 'fin' para terminar): ")
        if producto == 'fin':
            break
        if producto not in productos:
            print("Producto no encontrado.")
            continue
        cantidad = int(input("Cantidad: "))
        precio = productos[producto]
        
        venta["productos"].append({
            "nombre": producto,
            "cantidad": cantidad,
            "precio": precio
        })
    
    with open('data/ventas.json', 'a') as file:
        file.write(json.dumps(venta) + "\n")
    print("Venta registrada con éxito.")