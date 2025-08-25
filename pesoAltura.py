# Pedir datos al usuario
peso = float(input("Ingresa tu peso en kilogramos (kg): "))
altura = float(input("Ingresa tu altura en metros (m): "))

# Calcular el IMC
imc = peso / (altura ** 2)

# Mostrar el resultado
print(f"\nTu Índice de Masa Corporal (IMC) es: {imc:.2f}")
