print("CALCULADORA DE IMC")
print()

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)

print()
print(f"Su IMC es: {imc:.2f}")

print()
if imc < 18.5:
    print("Clasificación: BAJO PESO")
elif imc >= 18.5 and imc < 25:
    print("Clasificación: PESO NORMAL")
elif imc >= 25 and imc < 30:
    print("Clasificación: SOBREPESO")
else:
    print("Clasificación: OBESIDAD")
