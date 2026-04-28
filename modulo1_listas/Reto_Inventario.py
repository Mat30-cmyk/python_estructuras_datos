# Inventario
inventario = [
    ["Laptop", 10, 2500],
    ["Mouse", 25, 50],
    ["Teclado", 15, 120]
]

# Buscar producto (helper simple con listas)
def buscar_producto(nombre):
    for item in inventario:
        if item[0].lower() == nombre.lower():
            return item
    return None

# Actualizar precio
def actualizar_precio(producto, nuevo_precio):
    item = buscar_producto(producto)
    if item:
        if nuevo_precio > 0:
            item[2] = nuevo_precio
        else:
            print("Precio inválido 😑")
    else:
        print("Producto no encontrado 🤡")

# Registrar venta
def registrar_venta(producto, cantidad):
    item = buscar_producto(producto)
    if item:
        if cantidad > 0:
            if item[1] >= cantidad:
                item[1] -= cantidad
            else:
                print("Stock insuficiente 💀")
        else:
            print("Cantidad inválida bro")
    else:
        print("Ese producto no existe 🥴")

# Añadir producto
def anadir_producto(producto, cantidad, precio):
    if cantidad <= 0 or precio <= 0:
        print("Datos inválidos 🚫")
        return

    item = buscar_producto(producto)
    if item:
        item[1] += cantidad
        print("Stock actualizado 👍")
    else:
        inventario.append([producto, cantidad, precio])
        print("Producto agregado 🚀")

# Mostrar inventario bonito
def mostrar_inventario():
    print("\n=== INVENTARIO ===")
    for i, item in enumerate(inventario, 1):
        print(f"{i}. {item[0]:<10} | Stock: {item[1]:>3} | Precio: ${item[2]:>6.2f}")
    print("=================\n")

# 🔥 Pruebas
actualizar_precio("mouse", 60)
registrar_venta("Laptop", 2)
registrar_venta("Laptop", 100)  # error
anadir_producto("Monitor", 5, 800)
anadir_producto("Mouse", 5, 50)
mostrar_inventario()