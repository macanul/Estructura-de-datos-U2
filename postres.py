
POSTRES = [
    {"nombre": "Flan", "ingredientes": ["huevo", "leche", "azucar"]},
    {"nombre": "Gelatina", "ingredientes": ["agua", "gelatina", "azucar"]},
    {"nombre": "Pastel", "ingredientes": ["harina", "huevo", "leche"]},
    {"nombre": "Pay", "ingredientes": ["galletas", "mantequilla", "queso"]},
    {"nombre": "Flan", "ingredientes": ["huevo", "leche", "azucar"]},
]


def buscar_postre(nombre):
    for postre in POSTRES:
        if postre["nombre"].lower() == nombre.lower():
            return postre
    return None


def consultar_ingredientes():
    nombre = input("Nombre del postre: ")
    postre = buscar_postre(nombre)

    if postre is None:
        print("El postre no existe")
    else:
        print("Ingredientes de", postre["nombre"])

        if len(postre["ingredientes"]) == 0:
            print("Este postre no tiene ingredientes")
        else:
            for ingrediente in postre["ingredientes"]:
                print("-", ingrediente)


def agregar_ingrediente():
    nombre = input("Nombre del postre: ")
    postre = buscar_postre(nombre)

    if postre is None:
        print("El postre no existe")
        return

    ingrediente = input("Nuevo ingrediente: ").strip()

    if ingrediente == "":
        print("El ingrediente no puede estar vacio")
    elif ingrediente.lower() in [
        i.lower() for i in postre["ingredientes"]
    ]:
        print("El ingrediente ya existe")
    else:
        postre["ingredientes"].append(ingrediente)
        print("Ingrediente agregado correctamente")


def eliminar_ingrediente():
    nombre = input("Nombre del postre: ")
    postre = buscar_postre(nombre)

    if postre is None:
        print("El postre no existe")
        return

    if len(postre["ingredientes"]) == 0:
        print("El postre no tiene ingredientes")
        return

    ingrediente = input("Ingrediente que desea eliminar: ").strip()

    for i in range(len(postre["ingredientes"])):
        if postre["ingredientes"][i].lower() == ingrediente.lower():
            del postre["ingredientes"][i]
            print("Ingrediente eliminado correctamente")
            return

    print("El ingrediente no existe en este postre")


def alta_postre():
    nombre = input("Nombre del nuevo postre: ").strip()

    if nombre == "":
        print("El nombre no puede estar vacio")
        return

    if buscar_postre(nombre) is not None:
        print("El postre ya existe")
        return

    ingredientes = []

    try:
        cantidad = int(input("Cuantos ingredientes tiene: "))
    except ValueError:
        print("Debes escribir un numero entero")
        return

    if cantidad < 0:
        print("La cantidad no puede ser negativa")
        return

    for i in range(cantidad):
        ingrediente = input(
            "Ingrediente " + str(i + 1) + ": "
        ).strip()

        if ingrediente == "":
            print("El ingrediente no puede estar vacio")
            return

        ingredientes.append(ingrediente)

    nuevo_postre = {
        "nombre": nombre,
        "ingredientes": ingredientes
    }

    POSTRES.append(nuevo_postre)
    POSTRES.sort(key=lambda p: p["nombre"].lower())

    print("Postre agregado correctamente")


def baja_postre():
    nombre = input("Nombre del postre que desea eliminar: ")
    postre = buscar_postre(nombre)

    if postre is None:
        print("El postre no existe")
    else:
        POSTRES.remove(postre)
        print("Postre y sus ingredientes eliminados correctamente")


def mostrar_postres():
    if len(POSTRES) == 0:
        print("No hay postres registrados")
        return

    for postre in POSTRES:
        print(postre["nombre"], ":", postre["ingredientes"])


def menu():
    while True:
        print("\n--- MENU DE POSTRES ---")
        print("1. Consultar ingredientes")
        print("2. Agregar ingrediente")
        print("3. Eliminar ingrediente")
        print("4. Dar de alta un postre")
        print("5. Dar de baja un postre")
        print("6. Mostrar todos los postres")
        print("7. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            consultar_ingredientes()
        elif opcion == "2":
            agregar_ingrediente()
        elif opcion == "3":
            eliminar_ingrediente()
        elif opcion == "4":
            alta_postre()
        elif opcion == "5":
            baja_postre()
        elif opcion == "6":
            mostrar_postres()
        elif opcion == "7":
            print("Programa finalizado")
            break
        else:
            print("Opcion no valida")


if __name__ == "__main__":
    menu()
