"""
Realizar una aplicación en Python...
"""

# ENTRADA Lts_100km(float) - costo_lt (float) - longitud_viaje (float)
litros_por_100km = float(input(""))

costo_por_litro = float(input(""))

longitud_viaje = float(input(""))

# PROCESO - Calcular los litros consumidos y el precio final
litros_consumidos = (longitud_viaje * litros_por_100km) / 100

#costo total
costo_total = litros_consumidos * costo_por_litro

# SALIDA - Litros consumidos y el precio final
print(f"...: {litros_consumidos} 1")
print(f"... : $")