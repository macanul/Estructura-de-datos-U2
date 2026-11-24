def registrar_participantes(participantes):
    cantidad = int(input("¿Cuántos participantes deseas registrar?: "))

    for i in range(cantidad):
        dorsal = int(input("Ingresa el número de dorsal: "))

        repetido = False

        for participante in participantes:
            if participante[0] == dorsal:
                repetido = True
                break

        if repetido:
            print("Ese número de dorsal ya está registrado.")
        else:
            nombre = input("Ingresa el nombre del participante: ")
            participantes.append([dorsal, nombre])

    # Ordenar participantes por número de dorsal
    participantes.sort(key=lambda participante: participante[0])

    print("Registro actualizado correctamente.")


def mostrar_participantes(participantes):
    if len(participantes) == 0:
        print("No hay participantes registrados.")
    else:
        print("\n--- PARTICIPANTES ---")

        for participante in participantes:
            print("Dorsal:", participante[0],
                  "- Nombre:", participante[1])


def busqueda_binaria(participantes):
    if len(participantes) == 0:
        print("No hay participantes para buscar.")
        return

    buscar = int(input("Ingresa el número de dorsal que buscas: "))

    inicio = 0
    fin = len(participantes) - 1
    encontrado = False

    while inicio <= fin:
        medio = (inicio + fin) // 2

        if participantes[medio][0] == buscar:
            print("\nParticipante encontrado.")
            print("Dorsal:", participantes[medio][0])
            print("Nombre:", participantes[medio][1])
            encontrado = True
            break

        elif participantes[medio][0] < buscar:
            inicio = medio + 1

        else:
            fin = medio - 1

    if encontrado == False:
        print("No se encontró ese número de dorsal.")


# PROGRAMA PRINCIPAL
participantes = []

while True:
    print("\n===== REGISTRO DE CARRERA =====")
    print("1. Registrar participantes")
    print("2. Mostrar participantes")
    print("3. Buscar participante (Binaria)")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        registrar_participantes(participantes)

    elif opcion == "2":
        mostrar_participantes(participantes)

    elif opcion == "3":
        busqueda_binaria(participantes)

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida.")
