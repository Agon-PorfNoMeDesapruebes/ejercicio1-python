

"""1. Escribe un programa que identifique el color
de un objeto y muestre un mensaje según el color."""
"""
pregunta = input("pone un color")
if pregunta == "rojo":
    print("El color es rojo")
elif pregunta == "azul":
    print("El color es azul")
elif pregunta == "verde":
    print("El color es verde")
elif pregunta == "morado":
    print("El color es morado")
elif pregunta == "amarillo":
    print("El color es amirillo")
elif pregunta == "celeste":
    print("El color es celeste")
elif pregunta == "sian":
    print("El color es sian")
else:
    print("perdon pero no identifico ese color")    
"""
"""2. Escribe un programa que muestre
los números del 0 al 4 usando un ciclo while."""
"""
numero = [0,1,2,3,4]
n = 0
while n<=5:
    print(numero[n])
    n += 1
"""
"""
2.1. Escribe un programa que solicita al usuario
que ingrese números enteros positivos y muestre
la suma de esos números. La entrada de números
continuará hasta que el usuario ingrese un 
número negativo, momento en el que el programa 
mostrará la suma total.
"""
"""
suma = 0
valor = True
while valor :
    numero = input("ingresa un numero")
    if numero < 0 :
        valor == False
    else:
        suma+=numero
"""
"""3.Escribe un programa que muestra la primer,
última u otra letra de una cadena de carcateres,
inclusive una rebanada."""
"""
cadena = input("Escrive lo que quieras rebanar")
print(cadena[0])
print(cadena[-1])
largo = len(cadena)
print(cadena[largo//4 : largo//2])
print(len(cadena))"""
"""4. Crear una lista de frutas y mostrar en consola
algunas frutas de la lista, también por rebanadas."""
"""
frutas = ["mansana", "pera", "durazno", "anana"]
print(frutas[0])
print(frutas[-1])
print(frutas[1: -1])"""
"""5. Escribe un programa que recorra una lista de 
frutas y muestre cada fruta."""

"""
frutas = ["mansana", "pera", "durazno", "anana"]
for i in frutas:
    print(i)
    agregar = input("queres agregar algo más(si, no)" )
    if agregar in ["si", "Si", "Sí", "sí"]:
        nueva = input("escribe la fruta que quieras agregar: ")
        frutas.append(nueva)
    else:
        print("")
    saber = input("¿Quieres averiguar una especifica?(si,no) ")
    if saber in ["si", "Si", "Sí", "sí"]:
        conocer = input("Escribe la que quieras saber: ")
        if conocer in frutas :
            indice = frutas.index(conocer)
            print(f"{conocer} esta en el subindice {indice}")
        else:
            print("Lo sentimos pero no esta" )
    else: ""
"""
"""5.1 Agregar otras frutas a la lista."""
"""5.2 Escribe un programa verifique si una fruta 
específica está en una lista de frutas y muestra
un mensaje correspondiente."""
"""6. Escribe un programa que recorra una lista
de números y muestre si cada número es par o impar."""
"""
numeros = [2,5,4,6,3,4,6,345,354,32,35,75,46,34]
for i in numeros:
    pares = i % 2 == 0
    print(pares)
"""
"""7. Escribe un programa que recorra una cadena de 
texto y cuente cuántas veces aparece la letra 'a' en la cadena.
"""
"""
cadena = "basta amigo"
veces = 0
for i in cadena :
    if i == "a" :
        veces += 1
        print(veces)
    else: ""
"""
"""8. Integrador:
Escribe un programa que permita a un usuario crear
una lista de nombres. El programa continuará pidiendo
nombres hasta que el usuario ingrese "fin". Luego, 
el programa mostrará la lista de nombres en orden alfabético,
indicará cuántos nombres empiezan con la letra 'A' o 'E', 
y mostrará si un nombre específico está en la lista."""
"""
dondeSeGuarda = []
lista = input("Eres libre de agregar todos loss nombres que quieras, en caso de querer dejar de hacerlo escribe (fin)" )
while lista != "fin" :
    dondeSeGuarda.append(lista)
    lista = input("Eres libre de agregar todos loss nombres que quieras, en caso de querer dejar de hacerlo escribe (fin)" )
if "fin" in lista :
    print(dondeSeGuarda)
    orden = sorted(dondeSeGuarda)
    print(orden)
    contador = 0
    for i in orden :
        if i[0] in ["A", "E"] :
            contador += 1
    print(f"hay {contador} nombres que empiezan con A o E")
    nombre = input("¿Quieres saber si un nombre esta en la lista? (si, no) ")
    if nombre in ["si", "Si", "Sí", "sí"] :
        consulta = input("Escribe el nombre que quieres consultar: ")
        if consulta in orden :
            print(f"{consulta} esta en la lista")
        else:
            print(f"{consulta} no esta en la lista")
"""
