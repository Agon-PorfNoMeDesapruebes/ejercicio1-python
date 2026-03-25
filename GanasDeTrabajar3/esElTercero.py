"""1. Define una lista de diccionarios que 
represente información personal.
nombre,edad. Luego, accede a
elementos específicos de la lista, 
como el primer diccionario, el nombre 
de la primera persona y la edad de la 
segunda persona, para finalmente imprimir
los resultados en la consola."""


"""
superDiccionario = [{'nombre':"bobito",'añitos':16
    },{'nombre':"caracol",'añitos':78
        },{'nombre':"sabueso",'añitos':1
            },{'nombre':"abue",'añitos':20
                },{'nombre':"lombris",'añitos':7
                    },{
                        'nombre':"fuaaaa",'añitos':1000
                    }]
primera_persona = superDiccionario[0]
print(f"Nombre de la primera persona: {superDiccionario[0]['nombre']}")
print(f"Añitos de la segunda persona: {superDiccionario[1]['añitos']}")
for k in superDiccionario:
    for v in k :
        print(f"Lo que muestra k es: {k}")
        print(f"Lo que muestra v es: {v}")
"""
"""1.2. Del punto 1, recorrer y mostrar k,v"""


"""# Funciones:
2. Definir función, parámetros, retorno,
capturar un valor o varios"""

"""
def funcionFuncionsosa(aumentar, disminuir) :
    suma = 0 + aumentar
    resta = 0 + disminuir
    resultado = suma - resta
    return resultado

seraSerieCrecienteODecreciente = funcionFuncionsosa(3, 1)
print(seraSerieCrecienteODecreciente)
"""

"""3. Contar palabras"""
"""
contadasUnaPorUna = 0
palabras = input("ingresa la palabra que quieras saber cuantas letras tiene: ")
for i in palabras:
    contadasUnaPorUna += 1
print(f"la cantidad de letras que tiene es la siguiente: {contadasUnaPorUna}")
"""

"""4. Verificación de Palíndromos"""

"""
palindromo = input("Ingrese su palabra: ")
palindromo2 = palindromo[::-1]
print(palindromo2)
if palindromo == palindromo2:
    print("Es un palindromo")
else:
    print("No es un palindromo")
"""

"""5. Lambda para sumar, potencia"""

"""
suma = lambda primero, segundo: primero + segundo
print(suma(2, 6))

potencia = lambda potenciado: potenciado ** 2
print(potencia(3))
"""

"""6. map() con lambda"""

"""
primero = [10, 7, 3]
segundo = [1, 9, 4]

promedioMayor = list(map(lambda primero, segundo: primero - segundo, primero, segundo))
print("La resta de cada columna da:", promedioMayor)

suma = sum(promedioMayor)
resultado = suma / 3
print(f"Suma de los elementos de promedioMayor: {suma}")
print(f"El resultado final: {resultado}") 
"""

"""7. Integrador: Crear programa que permita
al usuario agregar tareas con descripción, 
fecha límite y prioridad, así como mostrar 
la lista de tareas. 
Este menú se repite hasta que el usuario elige salir."""

"""
tareas = []

while True:
    print("\n¿Qué quieres hacer?")
    print("(1) Ver tareas")
    print("(2) Agregar tareas")
    print("(3) Salir")
    
    opcion = input("Elige una opción: ")

    if opcion == "3":
        print("¡Hasta luego!")
        break

    elif opcion == "1":
        print("\nLista completa de tareas:")
        for i in tareas:
            print(i)

    elif opcion == "2":
        while True:
            pregunta = input("\n¿Quieres agregar una tarea? (1 = si, 2 = no): ")
            if pregunta == "2":
                break
            elif pregunta != "1":
                print("No se entendió el mensaje")
            else:
                creacion1 = input("Agrega el nombre de la tarea: ")
                creacion2 = input("Describe la tarea: ")
                creacion3 = input("Fecha limite: ")
                creacion4 = input("Prioridad: ")
                nuevaTarea = {"nombre": creacion1, "descripcion": creacion2, "fecha": creacion3, "importancia": creacion4}
                tareas.append(nuevaTarea)
                print("Tarea agregada:", nuevaTarea)

    else:
        print("No se entendió el mensaje")

"""