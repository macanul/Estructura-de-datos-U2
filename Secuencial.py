def registrar_canciones(canciones):
    cantidad = int(input("¿Cuántas canciones deseas registrar?: "))

    for i in range(cantidad):
        cancion = input("Ingresa el nombre de la canción: ")
        canciones.append(cancion)

    print("Canciones registradas correctamente.")


def mostrar_canciones(canciones):
    if len(canciones) == 0:
        print("No hay canciones registradas.")
    else:
        print("\n--- LISTA DE REPRODUCCIÓN ---")

        for i in range(len(canciones)):
            print(i + 1, "-", canciones[i])


def busqueda_secuencial(canciones):
    if len(canciones) == 0:
        print("No hay canciones para buscar.")
        return

    buscar = input("Ingresa el nombre de la canción: ")

    encontrado = False

    for i in range(len(canciones)):
        if canciones[i].lower() == buscar.lower():
            print("\nCanción encontrada.")
            print("Nombre:", canciones[i])
            print("Posición:", i + 1)
            encontrado = True
            break

    if encontrado == False:
        print("La canción no se encuentra en la lista.")


# PROGRAMA PRINCIPAL
canciones = []

while True:
    print("\n===== LISTA DE REPRODUCCIÓN =====")
    print("1. Registrar canciones")
    print("2. Mostrar canciones")
    print("3. Buscar canción (Secuencial)")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        registrar_canciones(canciones)

    elif opcion == "2":
        mostrar_canciones(canciones)

    elif opcion == "3":
        busqueda_secuencial(canciones)

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida.")
