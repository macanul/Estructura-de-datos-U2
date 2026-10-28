
import postres


def eliminar_postres_repetidos():
    nombres = set()
    postres_sin_repetir = []

    for postre in postres.POSTRES:
        nombre = postre["nombre"].lower()

        if nombre not in nombres:
            nombres.add(nombre)
            postres_sin_repetir.append(postre)
        else:
            print("Postre repetido eliminado:", postre["nombre"])

    postres.POSTRES.clear()
    postres.POSTRES.extend(postres_sin_repetir)

    print("\nLista de postres sin repetidos:")
    postres.mostrar_postres()


if __name__ == "__main__":
    eliminar_postres_repetidos()
