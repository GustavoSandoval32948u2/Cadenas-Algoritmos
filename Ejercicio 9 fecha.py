fecha = input("Ingrese su fecha de nacimiento en formato dia/mes/año > ")

dia, mes, año = fecha.split("/")

print(f"Dia: {dia.zfill(2)}")
print(f"Mes: {mes.zfill(2)}")
print(f"Año: {año}")
