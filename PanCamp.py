import json

try:
    with open("reg_comprasVentas.json", "r") as openfile:
        registro = json.load(openfile)
except FileNotFoundError:
    print("Archivo no encontrado. Se creará uno nuevo.")
    registro = []
except json.JSONDecodeError:
    print("Archivo JSON vacío o mal formado. Se iniciará con una lista vacía.")
    registro = []

print("""
        ]|I{•------»   🥐  𝒫̾𝒶̾𝓃̾𝒞̾𝒶̾𝓂̾𝓅̾  🥐   »------•}I|[ 
""")

op = input("Seleccione una opción (1 para registrar una venta): ")

if op == "1":
    fCompra = input("Fecha de compra: ")
    iClient = input("Nombre del cliente: ")
    inClient = input("Dirección del cliente: ")
    eVenta = input("Nombre del empleado que realizó la venta: ")
    emVenta = input("Cargo del empleado que realizó la venta: ")
    pVendido = input("Nombre del producto: ")
    prVendido = input("Cantidad del producto: ")
    proVendido = input("Precio del producto: ")

    venta = {
        "Fecha de la venta": fCompra,
        "Información del cliente": {
            "Nombre del cliente": iClient,
            "Dirección del cliente": inClient
        },
        "Información del empleado que realizó la venta": {
            "Nombre del empleado": eVenta,
            "Cargo del empleado": emVenta
        },
        "Productos vendidos": {
            "Nombre del producto": pVendido,
            "Cantidad del producto": prVendido,
            "Precio del producto": proVendido
        }
    }

    registro.append(venta)

    # Guardar el registro actualizado en el archivo JSON
    with open("reg_comprasVentas.json", "w") as f:
        json.dump(registro, f, indent=4)
else:
    print("Opción no válida.")
