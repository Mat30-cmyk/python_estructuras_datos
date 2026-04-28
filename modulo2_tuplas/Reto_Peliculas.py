# Catálogo (tupla de tuplas)
catalogo = (
    ("Inception", "Nolan", 2010, 9.0),
    ("Interstellar", "Nolan", 2014, 9.5),
    ("Titanic", "Cameron", 1997, 8.5),
    ("Avatar", "Cameron", 2009, 8.0)
)

# 1. Mostrar catálogo
for titulo, director, año, puntuacion in catalogo:
    print(f"{titulo} - {director} ({año}) ⭐ {puntuacion}")

# 2. Separar primera del resto
primera, *resto = catalogo
print("\nPrimera:", primera)
print("Cantidad resto:", len(resto))

# 3. Buscar por director (más robusto)
def buscar_por_director(director):
    resultado = ()
    for peli in catalogo:
        if peli[1].lower() == director.lower().strip():
            resultado = resultado + (peli,)  # concatenar tuplas
    return resultado

# 4. Estadísticas (más seguro)
def obtener_estadisticas(peliculas):
    if len(peliculas) == 0:
        return 0, 0, 0

    puntuaciones = ()
    for peli in peliculas:
        puntuaciones = puntuaciones + (peli[3],)

    minimo = puntuaciones[0]
    maximo = puntuaciones[0]
    suma = 0

    for p in puntuaciones:
        if p < minimo:
            minimo = p
        if p > maximo:
            maximo = p
        suma += p

    promedio = suma / len(puntuaciones)

    return minimo, maximo, promedio

# 5. Pruebas
coincidencias = buscar_por_director("  nolan ")
if len(coincidencias) > 0:
    print("\nPelículas encontradas:")
    for titulo, director, año, puntuacion in coincidencias:
        print(f"{titulo} ⭐ {puntuacion}")
else:
    print("\nNo se encontraron películas 🤡")

minima, maxima, promedio = obtener_estadisticas(catalogo)
print(f"\nMin: {minima} | Max: {maxima} | Prom: {promedio:.2f}")