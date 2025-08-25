import math  # Importamos el módulo math para usar pi

# Pedir al usuario que ingrese el radio del círculo
radio = float(input("Ingresa el radio del círculo: "))

# Calcular el área (A = π * r²) y el perímetro (P = 2 * π * r)
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio

# Imprimir los resultados
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")
