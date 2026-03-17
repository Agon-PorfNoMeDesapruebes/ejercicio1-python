import os
os.system("clear")

"""1. Escribe un programa que imprima un 
mensaje personalizado en la pantalla
utilizando la función print().
"""

personalizado = print("Ahhhhh")

"""2. Escribe un programa que le pida al usuario
su nombre y luego lo imprima en la pantalla.
"""

nombre = input("¿Cuál es tu nombre? ")
print("Tu nombre es: ", nombre)

"""
3. Escribe un programa que realice operaciones
aritméticas simples, como suma, resta, 
multiplicación y división, utilizando 
números enteros y flotantes.
"""

numero1 = float(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
print(f"La suma es: {suma}, la resta es: {resta}, la multiplicacion es: {multiplicacion} y la division es: {division}")

"""4. Escribe un programa que tome dos cadenas de
texto (strings) como entrada del usuario y las
concatene, luego imprime el resultado."""

cadena = input("escribe lo que quieras unir:")
cadena2 = input("bien ahi")
print(cadena + cadena2)

"""6. Escribe un programa que utilice operadores
de asignación para realizar operaciones como 
incrementar o decrementar el valor de una variable."""

"""
numero =input("¿Quieres iterar un numero? (SI/NO) ")

if numero == "SI" or numero == "si" or numero == "Si" or numero == "sí":
    numeroUsado = float(input("Introduce un numero: "))
    while numero == "SI" or numero == "si" or numero == "Si" or numero == "sí":
        incrementar = input("¿Para incrementar el numero prseiona 1, para disminuir apleta 2? ")
        if incrementar == "1":
            numeroUsado += 1
            print("El numero es: ", numeroUsado)
            pregunta = input("¿Quieres volver a iterar el numero? (SI/NO) ")
            numero = pregunta
            cambiar = input(f"¿Quieres cambiar el numero? (SI/NO) ")
            if cambiar == "SI" or cambiar == "si" or cambiar == "Si" or cambiar == "sí":
                numeroUsado = float(input("Introduce un numero: "))
        elif incrementar == "2":
            numeroUsado -= 1
            print("El numero es: ", numeroUsado)
            pregunta = input("¿Quieres volver a iterar el numero? (SI/NO) ")
            numero = pregunta
            cambiar = input(f"¿Quieres cambiar el numero? (SI/NO) ")
            if cambiar == "SI" or cambiar == "si" or cambiar == "Si" or cambiar == "sí":
                numeroUsado = float(input("Introduce un numero: "))
"""

"""7. crear un programa que le pida al usuario
nombre, edad y ciudad de residencia, realizar
cálculos basados en la edad, y luego mostrará
la información en pantalla 
(# Pedir al usuario que ingrese su nombre
# Pedir al usuario que ingrese su edad
# Pedir al usuario que ingrese su ciudad de residencia
# Calcular el año de nacimiento
# Saludar al usuario y mostrar la información
# Comprobar si la edad es mayor de 18 años
# Comprobar si la edad es un múltiplo de 5)."""

nombreUsuario = input("¿Cuál es tu nombre? ")
edadUsuario = int(input("¿Cuál es tu edad? "))
ciudadUsuario = input("¿Cuál es tu ciudad de residencia? ")
añoNacimiento = 2026 - edadUsuario
if edadUsuario > 18 and edadUsuario % 5 == 0:
    print(f"Hola {nombreUsuario}, naciste en el año {añoNacimiento} y vives en {ciudadUsuario}. Además, eres mayor de edad y tu edad es un múltiplo de 5.")
elif edadUsuario > 18 and edadUsuario % 5 != 0:
    print(f"Hola {nombreUsuario}, naciste en el año {añoNacimiento} y vives en {ciudadUsuario}. Además, eres mayor de edad pero tu edad no es un múltiplo de 5.")
elif edadUsuario <= 18 and edadUsuario % 5 == 0:
    print(f"Hola {nombreUsuario}, naciste en el año {añoNacimiento} y vives en {ciudadUsuario}. No eres mayor de edad pero tu edad es múltiplo de 5.")
else:
    print(f"Hola {nombreUsuario}, naciste en el año {añoNacimiento} y vives en {ciudadUsuario}. No eres mayor de edad y tu edad no es un múltiplo de 5.")

"""8.  crearemos un programa que verifica si
un número ingresado por el usuario es positivo,
negativo o cero, y también si es un número par o impar."""

numeroPregunta = float(input("dame un numero"))
if numeroPregunta < 0:
    print("tu numero es negativo")
elif numeroPregunta > 0:
    print("tu numero es positivo")
elif numeroPregunta == 0:
    print("tu numero es 0")
if numeroPregunta % 2 == 0:
    print("tu numero es par")
elif numeroPregunta % 2 == 1:
    print("tu numero es impar")