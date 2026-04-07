"""
"""
def agregar_tarea(tareas, tarea, fecha_limite, prioridad, completada = False):
    nueva_tarea = {"Tarea": tarea, "Fecha limite": fecha_limite, "Prioridad": prioridad, "Estado": completada}
    tareas.append(nueva_tarea)
    print("Tarea agregada exitosamente.")

def marcar_completada(tareas):
    if not tareas:
        print("No hay tareas para marcar.")
        return

    print("Ingresa cual tarea quieres marcar como completada: ")
    numero = input()

    if numero.isdigit():
        indice = int(numero) - 1

        if indice >= 0 and indice < len(tareas):
            tareas[indice]["Estado"] = True
            print("Tarea marcada como completada.")
        else:
            print("Número inválido.")
    else:
        print("Debes ingresar un número.")

def pedir_fecha():
    while True:
        fecha = input("Ingrese la fecha limite (formato: dd/mm/yyyy): ")
        partes = fecha.split("/")
        
        if len(partes) == 3 and all(p.isdigit() for p in partes):
            dia, mes, anio = int(partes[0]), int(partes[1]), int(partes[2])
            
            if 1 <= dia <= 31 and 1 <= mes <= 12 and anio >= 2025:
                return fecha
        
        print("Formato inválido. Use dd/mm/yyyy (ej: 25/12/2025)")

def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        cuestion = input("Quieres ver solamente las completas (1), solamente las que no lo estan (2) o todas (3): ")
        if cuestion == "1":
            for i, tarea in enumerate(tareas, 1):
                if tarea["Estado"] == True:
                    print(f"\nTarea {i}:")
                    for clave, valor in tarea.items():
                        print(f"{clave}: {valor}")
        elif cuestion == "2":
            for i, tarea in enumerate(tareas, 1):
                if tarea["Estado"] == False:
                    print(f"\nTarea {i}:")
                    for clave, valor in tarea.items():
                        print(f"{clave}: {valor}")
        elif cuestion == "3":
            for i, tarea in enumerate(tareas, 1):
                print(f"\nTarea {i}:")
                for clave, valor in tarea.items():
                    print(f"{clave}: {valor}")
        


if __name__ == "__main__":
    lista_tareas = []

    while True:
        print("\n1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Marcar completada")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tarea_nueva = input("Ingrese la descripción de la tarea: ")
            fecha_limite_nueva = pedir_fecha()
            prioridad_nueva = input("Ingrese la prioridad: ")
            agregar_tarea(lista_tareas, tarea_nueva, fecha_limite_nueva, prioridad_nueva)

        elif opcion == "2":
            mostrar_tareas(lista_tareas)

        elif opcion == "3":
            marcar_completada(lista_tareas)

        elif opcion == "4":
            break

        else:
            print("Opción no válida. Intente nuevamente.")



