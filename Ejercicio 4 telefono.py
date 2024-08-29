telefono = input("Ingrese su numero de telefono incluyendo su prefijo y extension > ")

partes = telefono.split("-")

numero_sin_prefijo_y_extension = partes[1]

print("El número sin prefijo ni extensión es:", numero_sin_prefijo_y_extension)
