print("CONVERSOR DE TEMPERATURA")
print("Opciones de conversión:")
print("1. Celsius a Fahrenheit")
print("2. Fahrenheit a Celsius")

opcion = input("Seleccione una opción (1 o 2): ")

if opcion == "1":

    print("\n--- Celsius a Fahrenheit ---")
    celsius = float(input("Ingrese la temperatura en Celsius: "))
    
    fahrenheit = celsius * 1.8 + 32
    
    print(f"\n{celsius}°C = {fahrenheit:.2f}°F")

elif opcion == "2":
    print("\n--- Fahrenheit a Celsius ---")
    fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
    
    celsius = (fahrenheit - 32) / 1.8
    
    print(f"\n{fahrenheit}°F = {celsius:.2f}°C")

else:
    print("\nOpción no válida. Por favor, seleccione 1 o 2.")

print("\n¡Gracias por usar el conversor de temperatura!")
