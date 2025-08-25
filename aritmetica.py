# Pedir dos números enteros distintos de 0
num1 = int(input("Ingresa el primer número (distinto de 0): "))
num2 = int(input("Ingresa el segundo número (distinto de 0): "))

# Verificar que ninguno sea cero
if num1 != 0 and num2 != 0:
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2  # División real con decimales

    # Mostrar los resultados
    print(f"\nResultados:")
    print(f"{num1} + {num2} = {suma}")
    print(f"{num1} - {num2} = {resta}")
    print(f"{num1} * {num2} = {multiplicacion}")
    print(f"{num1} / {num2} = {division:.2f}")
else:
    print("Error: ambos números deben ser distintos de 0.")
