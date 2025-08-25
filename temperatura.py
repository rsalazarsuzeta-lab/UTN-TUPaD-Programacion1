# Pedir al usuario una temperatura en grados Celsius
celsius = float(input("Ingresa la temperatura en grados Celsius: "))

# Convertir a grados Fahrenheit
fahrenheit = (9 / 5) * celsius + 32

# Mostrar el resultado
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")
