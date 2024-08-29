
productos = input("Introduce una lista de productos de la cesta de compra, separados por comas: ")

lista_productos = productos.split(",")

for i in lista_productos:
    print(i.strip())
