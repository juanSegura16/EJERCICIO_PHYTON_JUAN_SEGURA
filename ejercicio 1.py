precio = float(input("Ingrese el precio del artículo (debe ser número decimal): "))
cantidad = int(input("Ingrese la cantidad de unidades que desea comprar: "))

costo_total = precio * cantidad

print(f"El costo total de su compra es: {costo_total:.3f} pesos.")
