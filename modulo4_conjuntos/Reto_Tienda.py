# 1. Tiendas
tienda_centro = {"Laptop", "Mouse", "Teclado", "Monitor"}
tienda_norte  = {"Mouse", "Teclado", "Audifonos", "Webcam"}
tienda_sur    = {"Laptop", "Monitor", "Impresora", "Webcam"}

# 2. Catálogo completo
catalogo_completo = tienda_centro.union(tienda_norte).union(tienda_sur)

# 3. Productos comunes
productos_comunes = tienda_centro.intersection(tienda_norte).intersection(tienda_sur)

# 4. Exclusivos
exclusivo_centro = tienda_centro.difference(tienda_norte.union(tienda_sur))
exclusivo_norte  = tienda_norte.difference(tienda_centro.union(tienda_sur))
exclusivo_sur    = tienda_sur.difference(tienda_centro.union(tienda_norte))

# 5. Verificar solapamientos
print("Centro y Norte comparten:", tienda_centro.intersection(tienda_norte))
print("Centro y Sur comparten:", tienda_centro.intersection(tienda_sur))
print("Norte y Sur comparten:", tienda_norte.intersection(tienda_sur))

# 6. Usuarios
usuario1 = {"Accion", "Comedia", "Drama"}
usuario2 = {"Comedia", "Terror", "Drama"}
usuario3 = {"Accion", "Ciencia Ficcion", "Aventura"}

# 7. Operaciones
comunes = usuario1 & usuario2
todos = usuario1 | usuario2 | usuario3
solo_u1 = usuario1 - usuario2
dif = usuario2 ^ usuario3

# 8. Subconjunto
print("u1 es subconjunto de todos?", usuario1 <= todos)

# 9. Reporte simple
print("\nCATALOGO:", catalogo_completo)
print("COMUNES:", productos_comunes)

print("\nEXCLUSIVOS:")
print("Centro:", exclusivo_centro)
print("Norte:", exclusivo_norte)
print("Sur:", exclusivo_sur)

print("\nUSUARIOS:")
print("Comunes u1-u2:", comunes)
print("Todos:", todos)
print("Solo u1:", solo_u1)
print("Dif u2-u3:", dif)