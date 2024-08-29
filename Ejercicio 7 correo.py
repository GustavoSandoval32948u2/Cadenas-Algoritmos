correo = input("Ingrese su correo electronico > ")

correo_nuevo = correo.replace(correo.split("@")[1],"ceu.es")

print(f"El nuevo correo es {correo_nuevo}")
