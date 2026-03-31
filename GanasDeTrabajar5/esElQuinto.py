"""
    1- Calculadora de índice de masa corporal (IMC):
- Solicita al usuario que ingrese su peso en kg y su altura en metros.
- Calcula el IMC utilizando la fórmula: IMC = peso / (altura * altura).
- Muestra el IMC calculado y una categoría de peso según el IMC (talla s, talla m, talla l, talla xl).
53 1.52
"""
"""

peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))

def IMC(altura, peso):
    calculoIMC = float((peso / (altura * altura)))
    if calculoIMC <= 25:
        categoria = "Sos talla s"
    elif calculoIMC <= 30:
        categoria = "Sos talla m"
    elif calculoIMC <= 35:
        categoria = "Sos talla l"
    else: 
        categoria = "Obeso come torta"
    
    return calculoIMC, categoria

print(IMC(altura,peso))

"""
"""2- Conversor de temperaturas:
Pide al usuario que ingrese una temperatura en grados Celsius.
Convierte la temperatura a grados Fahrenheit utilizando la fórmula: Fahrenheit = (Celsius * 9/5) + 32.
Imprime la temperatura en grados Fahrenheit.
"""

"""
celsius = float(input("Ingresa los grados Celsius: "))

def calcular(celsius):
    Fahrenheit = float((celsius * 9/5) + 32)
    
    return Fahrenheit

print(calcular(celsius))

"""

"""3- Generador de secuencia Fibonacci:
Pide al usuario que ingrese un número entero positivo.
Genera los primeros n números de la secuencia Fibonacci, donde n es el número ingresado por el usuario.
Muestra la secuencia Fibonacci resultante.
"""


"""
entero = int(input("Ingresa un valor entero positivo: "))

def fibonacci(terminos):
    if terminos <= 0:
        return []
    if terminos == 1:
        return [0]

    sequencia = [0, 1]
    for i in range(2, terminos):
        sequencia.append(sequencia[i - 1] + sequencia[i - 2])

    return sequencia


if entero <= 0:
    print("Debes ingresar un entero positivo mayor que 0.")
else:
    print(f"Los primeros {entero} términos de Fibonacci son: {fibonacci(entero)}")

"""


"""4- Validador de contraseña:
Solicita al usuario que cree una contraseña.
Verifica si la contraseña cumple con los siguientes criterios:
Tiene al menos 8 simboloes de longitud.
Contiene al menos una letra mayúscula y una letra minúscula.
Tiene al menos un número.
Tiene al menos un carácter especial (por ejemplo, !, @, #, $, %, etc.).
Informa al usuario si la contraseña es válida o no.
"""

"""
contraseña = input("Ingresa tu contraseña: ")

def verificacion(contraseña):

    if len(contraseña) < 8:
        return False

    tieneMayuscula = False
    tieneMinuscula = False
    tieneNumero = False
    tieneEspecial = False

    for simbolo in contraseña:
        if simbolo.isupper():
            tieneMayuscula = True
        elif simbolo.islower():
            tieneMinuscula = True
        elif simbolo.isdigit():
            tieneNumero = True
        else:
            tieneEspecial = True

    if tieneMayuscula and tieneMinuscula and tieneNumero and tieneEspecial:
        return True
    else:
        return False

if verificacion(contraseña):
    print("Contraseña válida")
else:
    print("Contraseña inválida")

"""


"""5- Juego de adivinanza de números:
Genera un número aleatorio entre 1 y 100.
Pide al usuario que adivine el número.
Proporciona pistas al usuario si el número es demasiado alto o demasiado bajo.
Continúa solicitando al usuario que adivine hasta que lo haga correctamente.
Muestra el número de intentos necesarios para adivinar.
"""

"""
import random

pregunta = True
numero = random.randint(1, 100)
intentos = 0

def ver(numero, numeroPedido, pregunta):
    diferencia = numeroPedido - numero

    if diferencia == 0:
        print("¡Correcto!")
        return False

    elif diferencia > 0:
        if diferencia >= 80:
            print("Es mucho más bajo")
        elif diferencia >= 20:
            print("Es más bajo")
        elif diferencia >= 5:
            print("Es un poquito más bajo, casi lo tienes")

    elif diferencia < 0:
        if diferencia <= -80:
            print("Es mucho más alto")
        elif diferencia <= -20:
            print("Es más alto")
        elif diferencia <= -5:
            print("Es un poquito más alto, casi lo tienes")

    preguntita = input("¿Desea seguir? 1: si, 2: no: ")
    if preguntita == "1":
        return True
    else:
        return False

while pregunta:
    numeroPedido = int(input("Ingrese un número: "))
    intentos += 1
    pregunta = ver(numero, numeroPedido, pregunta)

if numeroPedido == numero:
    print(f"Adivinaste el número en {intentos} intentos")
else:
    print(f"Juego terminado. El número era {numero}")


"""

"""6- Administrador de tareas:
Permite al usuario agregar tareas con una descripción y una fecha de vencimiento.
Muestra la lista de tareas agregadas.
Permite al usuario marcar una tarea como completada y eliminar tareas de la lista.
"""