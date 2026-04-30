# 1. Dataset
ventas = [
    {"producto":"laptop","unidades":10,"precio":800,"categoria":"tecnologia"},
    {"producto":"mouse","unidades":30,"precio":20,"categoria":"tecnologia"},
    {"producto":"teclado","unidades":20,"precio":50,"categoria":"tecnologia"},
    {"producto":"monitor","unidades":5,"precio":200,"categoria":"tecnologia"},
    {"producto":"silla","unidades":15,"precio":150,"categoria":"muebles"},
    {"producto":"cuaderno","unidades":50,"precio":5,"categoria":"papeleria"}
]

# 2. List comp: valor total
valores = [v["unidades"] * v["precio"] for v in ventas]

# 3. List comp con filtro
productos_destacados = [
    v["producto"]
    for v in ventas
    if v["unidades"] * v["precio"] > 1000
]

# 4. Dict comp: info
producto_info = {
    v["producto"]: {
        "valor": v["unidades"] * v["precio"],
        "unidades": v["unidades"]
    }
    for v in ventas
}

# 5. Dict comp con filtro (premium)
ranking_premium = {
    v["producto"]: v["unidades"] * v["precio"]
    for v in ventas
    if v["precio"] > 50
}

# 6. Set comp
categorias_unicas = {v["categoria"] for v in ventas}

# 7. Set comp con filtro
productos_baratos = {
    v["producto"]
    for v in ventas
    if v["precio"] <= 50
}

# 8. Resumen formateado
resumen_formateado = {
    v["producto"]: v["unidades"] * v["precio"]
    for v in ventas
    if v["unidades"] * v["precio"] > 500
}

# 9. Gran total
gran_total = sum(valores)

# 10. Prints simples
print("Valores:", valores)
print("Destacados:", productos_destacados)
print("Info:", producto_info)
print("Premium:", ranking_premium)
print("Categorías:", categorias_unicas)
print("Baratos:", productos_baratos)
print("Resumen:", resumen_formateado)
print("Gran total:", gran_total)