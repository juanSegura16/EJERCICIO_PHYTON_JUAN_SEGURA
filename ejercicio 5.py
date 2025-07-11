print("=== CONVERSOR DE TEMPERATURA ===")
print("Opciones de conversión:")
print("1. Celsius a Fahrenheit")
print("2. Fahrenheit a Celsius")

# Solicitar opción al usuario
opcion = input("Seleccione una opción (1 o 2): ")

if opcion == "1":
    # Conversión de Celsius a Fahrenheit
    print("\n--- Celsius a Fahrenheit ---")
    celsius = float(input("Ingrese la temperatura en Celsius: "))
    
    # Aplicar fórmula: F = C × 1.8 + 32
    fahrenheit = celsius * 1.8 + 32
    
    # Mostrar resultado
    print(f"\n{celsius}°C = {fahrenheit:.2f}°F")

elif opcion == "2":
    # Conversión de Fahrenheit a Celsius
    print("\n--- Fahrenheit a Celsius ---")
    fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
    
    # Aplicar fórmula: C = (F - 32) / 1.8
    celsius = (fahrenheit - 32) / 1.8
    
    # Mostrar resultado
    print(f"\n{fahrenheit}°F = {celsius:.2f}°C")

else:
    # Opción no válida
    print("\nOpción no válida. Por favor, seleccione 1 o 2.")

print("\n¡Gracias por usar el conversor de temperatura!")