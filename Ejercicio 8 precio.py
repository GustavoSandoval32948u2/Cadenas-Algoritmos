precio = input("Introduzca el precio de un producto que incluya 2 decimales: ")

euros, centimos = precio.split(".")

print(f"Euros: {euros}")
print(f"Centimos: {centimos}")
