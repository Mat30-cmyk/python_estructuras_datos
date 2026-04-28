# 1. Datos
ventas_por_region = {
    "Norte":  {"Q1": 1500, "Q2": 2000, "Q3": 1800, "Q4": 2200},
    "Sur":    {"Q1": 1200, "Q2": 1700, "Q3": 1600, "Q4": 2100},
    "Este":   {"Q1": 1000, "Q2": 1400, "Q3": 1300, "Q4": 1900},
    "Oeste":  {"Q1": 1800, "Q2": 2100, "Q3": 2000, "Q4": 2500}
}

# 2. Totales por región (validando datos)
totales = {}
for region, datos in ventas_por_region.items():
    total = 0
    for trimestre, valor in datos.items():
        if isinstance(valor, (int, float)) and valor >= 0:
            total += valor
        else:
            print(f"Valor inválido en {region}-{trimestre} 🤨")
    totales[region] = total

# 3. Mejor región (evitar error si vacío)
if len(totales) > 0:
    mejor_region = max(totales, key=lambda r: totales[r])
else:
    mejor_region = None

# 4. Totales por trimestre (dinámico)
totales_por_trimestre = {}

for region, datos in ventas_por_region.items():
    for trimestre, valor in datos.items():
        totales_por_trimestre.setdefault(trimestre, 0)
        if isinstance(valor, (int, float)):
            totales_por_trimestre[trimestre] += valor

# 5. Gran total seguro
gran_total = sum(totales.values())

# 6. Porcentajes seguros (evita división por 0)
if gran_total > 0:
    porcentajes = {
        region: round((total / gran_total) * 100, 2)
        for region, total in totales.items()
    }
else:
    porcentajes = dict.fromkeys(totales.keys(), 0)

# 7. Reporte ordenado y limpio
print("\n=== REPORTE DE VENTAS PRO 😎 ===")

for region, total in sorted(totales.items(), key=lambda x: x[1], reverse=True):
    pct = porcentajes.get(region, 0)
    print(f"{region}: ${total} ({pct}%)")

if mejor_region:
    print("\n🏆 Mejor región:", mejor_region)
else:
    print("\nNo hay datos bro 💀")

print("\n📊 Ventas por trimestre:")
for t, v in sorted(totales_por_trimestre.items()):
    print(f"{t}: ${v}")