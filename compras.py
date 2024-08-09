import json

def registrar_compra(productos):
    fecha = input("Ingrese la fecha de la compra (YYYY-MM-DD): ")
    nombre_proveedor = input("Nombre del proveedor: ")
    contacto_proveedor = input("Contacto del proveedor: ")
    
    compra = {
        "fecha": fecha,
        "proveedor": {
            "nombre": nombre_proveedor,
            "contacto": contacto_proveedor
        },
        "productos": []
    }
    
    while True:
        producto = input("Nombre del producto (o 'fin' para terminar): ")
        if producto == 'fin':
            break
        cantidad = int(input("Cantidad: "))
        precio_compra = float(input("Precio de compra: "))
        
        if producto in productos:
            productos[producto] += cantidad
        else:
            productos[producto] = cantidad
        
        compra["productos"].append({
            "nombre": producto,
            "cantidad": cantidad,
            "precio_compra": precio_compra
        })
    
    with open('data/compras.json', 'a') as file:
        file.write(json.dumps(compra) + "\n")
    print("Compra registrada con éxito.")