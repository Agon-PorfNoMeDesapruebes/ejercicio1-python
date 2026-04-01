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

"""
from datetime import date, datetime


def mostrar_menu():
    print("\n===== ADMINISTRADOR DE TAREAS =====")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")
    print("===================================")


def agregar_tarea(tareas):
    descripcion = input("Descripción de la tarea: ").strip()
    if not descripcion:
        print("La descripción no puede estar vacía.")
        return

    while True:
        vencimiento_str = input("Fecha de vencimiento (DD/MM/AAAA): ").strip()
        try:
            vencimiento = datetime.strptime(vencimiento_str, "%d/%m/%Y").date()
            break
        except ValueError:
            print("Formato inválido. Usá DD/MM/AAAA (ej: 25/12/2025).")

    tarea = {
        "id": len(tareas) + 1,
        "descripcion": descripcion,
        "vencimiento": vencimiento,
        "completada": False,
    }
    tareas.append(tarea)
    print(f"✓ Tarea #{tarea['id']} agregada.")


def ver_tareas(tareas):
    if not tareas:
        print("\nNo hay tareas registradas.")
        return

    print(f"\n{'#':<4} {'Estado':<12} {'Vencimiento':<14} Descripción")
    print("-" * 60)

    hoy = date.today()
    for t in tareas:
        estado = "✓ Hecha" if t["completada"] else "○ Pendiente"
        dias = (t["vencimiento"] - hoy).days
        if not t["completada"]:
            if dias < 0:
                alerta = " ⚠ VENCIDA"
            elif dias <= 2:
                alerta = " ⚡ PRONTO"
            else:
                alerta = ""
        else:
            alerta = ""

        print(
            f"{t['id']:<4} {estado:<12} "
            f"{t['vencimiento'].strftime('%d/%m/%Y'):<14} "
            f"{t['descripcion']}{alerta}"
        )


def marcar_completada(tareas):
    ver_tareas(tareas)
    if not tareas:
        return

    try:
        num = int(input("\nNúmero de tarea a marcar como completada: "))
        tarea = next((t for t in tareas if t["id"] == num), None)
        if not tarea:
            print("Tarea no encontrada.")
        elif tarea["completada"]:
            print("La tarea ya está completada.")
        else:
            tarea["completada"] = True
            print(f"✓ Tarea #{num} marcada como completada.")
    except ValueError:
        print("Ingresá un número válido.")


def eliminar_tarea(tareas):
    ver_tareas(tareas)
    if not tareas:
        return

    try:
        num = int(input("\nNúmero de tarea a eliminar: "))
        tarea = next((t for t in tareas if t["id"] == num), None)
        if not tarea:
            print("Tarea no encontrada.")
        else:
            tareas.remove(tarea)
            print(f"✓ Tarea #{num} eliminada.")
    except ValueError:
        print("Ingresá un número válido.")


def main():
    tareas = []
    print("Bienvenido al Administrador de Tareas.")

    while True:
        mostrar_menu()
        opcion = input("Elegí una opción (1-5): ").strip()

        match opcion:
            case "1":
                agregar_tarea(tareas)
            case "2":
                ver_tareas(tareas)
            case "3":
                marcar_completada(tareas)
            case "4":
                eliminar_tarea(tareas)
            case "5":
                print("¡Hasta luego!")
                break
            case _:
                print("Opción inválida. Elegí entre 1 y 5.")


if __name__ == "__main__":
    main()
    
"""

"""7- Calculadora de descuento de compra:
Solicita al usuario que ingrese el precio original del artículo y el porcentaje de descuento.
Calcula el precio final después del descuento.
Muestra el precio final al usuario.
"""

"""

def descontar(monto):
    descuento = 0.10
    sacar = monto * descuento
    total = monto - sacar
    return total

def main():
    print("Bienvenido")

    while True:
        try:
            opcion = int(input("Pon el monto a descontar: "))
            precioModificado = descontar(opcion)
            print(precioModificado)
            break
        except:
            print("Ingresa un monto valido")

if __name__ == "__main__":
    main()
    

"""

"""8- Generador de contraseñas aleatorias:
Solicita al usuario que ingrese la longitud deseada para la contraseña.
Genera una contraseña aleatoria con la longitud especificada.
Utiliza caracteres alfanuméricos y caracteres especiales para mayor seguridad.
Muestra la contraseña generada al usuario.
"""

import random
import string

def contraseña(cantidad):
    chars = string.ascii_letters + string.digits + string.punctuation
    largo = []
    for _ in range(cantidad):
        largo.append(random.choice(chars))
    return ''.join(largo)

def main():
    print("Bienvenido.")

    while True:
        try:
            opcion = int(input("Pon la cantidad de caracteres que quieres que tenga su contraseña: "))
            cantidad = contraseña(opcion)
            print(f"Tu contraseña generada es: {cantidad}")
            break
        except ValueError:
            print("Por favor, ingrese un numero")

if __name__ == "__main__":
    main()
    
#La parte de los caracteres la pense yo pero le pedi las funciones de chars a la IA, porque no sabia como llamarlas.