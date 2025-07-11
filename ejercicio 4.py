print("=== CALCULADORA DE IMC ===")
print()

# Solicitar datos al usuario
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

# Calcular IMC usando la fórmula: IMC = peso(kg) / (altura(m))²
imc = peso / (altura ** 2)

# Mostrar el resultado
print()
print(f"Su IMC es: {imc:.2f}")


# Clasificar el IMC
print()
if imc < 18.5:
    print("Clasificación: BAJO PESO")
elif imc >= 18.5 and imc < 25:
    print("Clasificación: PESO NORMAL")
elif imc >= 25 and imc < 30:
    print("Clasificación: SOBREPESO")
else:
    print("Clasificación: OBESIDAD")