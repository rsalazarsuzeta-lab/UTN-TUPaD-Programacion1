######## →Nombre y Apellidos: Ronar Salazar Suzeta
################# →Matricula: 102183
#↓↓↓
#Programa N° 1: Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
#----------------------------------------------------------------------------------------------------
print ("Hola Mundo");


#↓↓↓
#Programa N° 2: Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
#----------------------------------------------------------------------------------------------------
#Pedir al usuario que ingrese su nombre
nombre = input("Por favor, ingresa tu nombre: ")

# Imprimir el saludo usando el nombre ingresado
print(f"¡Hola {nombre}!")


#↓↓↓
#Programa N° 3: Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
#----------------------------------------------------------------------------------------------------
# Solicitar los datos al usuario
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("¿Dónde vives?: ")

# Imprimir una oración con los datos ingresados
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")



#↓↓↓
#Programa N° 4: Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
#----------------------------------------------------------------------------------------------------
import math  # Importamos el módulo math para usar pi

# Pedir al usuario que ingrese el radio del círculo
radio = float(input("Ingrese el radio del círculo: "))

# Calcular el área (A = π * r²) y el perímetro (P = 2 * π * r)
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio

# Imprimir los resultados
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")



#↓↓↓
#Programa N° 5: Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
#----------------------------------------------------------------------------------------------------
# Pedir al usuario una cantidad de segundos
segundos = int(input("Ingresa una cantidad de segundos: "))

# Calcular cuántas horas hay en esa cantidad de segundos
horas = segundos / 3600  # 1 hora = 3600 segundos

# Mostrar el resultado
print(f"{segundos} segundos equivalen a {horas:.2f} horas.")



#↓↓↓
#Programa N° 6: Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
#----------------------------------------------------------------------------------------------------
# Pedir al usuario un número
numero = int(input("Ingresa un número: "))

# Imprimir la tabla de multiplicar del número ingresado
print(f"Tabla de multiplicar del {numero}:")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")





#↓↓↓
#Programa N° 7: Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
#----------------------------------------------------------------------------------------------------
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





#↓↓↓
#Programa N° 8: Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:
#𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔(𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2
#----------------------------------------------------------------------------------------------------
# Pedir datos al usuario
peso = float(input("Ingresa tu peso en kilogramos (kg): "))
altura = float(input("Ingresa tu altura en metros (m): "))

# Calcular el IMC
imc = peso / (altura ** 2)

# Mostrar el resultado
print(f"\nTu Índice de Masa Corporal (IMC) es: {imc:.2f}")






#↓↓↓
#Programa N° 9: Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
#𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 =95.𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32
#----------------------------------------------------------------------------------------------------
# Pedir al usuario una temperatura en grados Celsius
celsius = float(input("Ingresa la temperatura en grados Celsius: "))

# Convertir a grados Fahrenheit
fahrenheit = (9 / 5) * celsius + 32

# Mostrar el resultado
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")




#↓↓↓
#Programa N° 10: Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
#promedio = (num1 + num2 + num3) / 3
#----------------------------------------------------------------------------------------------------
# Pedir al usuario tres números
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

# Calcular el promedio
promedio = (num1 + num2 + num3) / 3

# Mostrar el resultado
print(f"El promedio de los tres números es: {promedio:.2f}")
