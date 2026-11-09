
def buscar(padres, nodo):
    if padres[nodo] != nodo:
        padres[nodo] = buscar(padres, padres[nodo])

    return padres[nodo]


def unir(padres, rangos, nodo1, nodo2):
    raiz1 = buscar(padres, nodo1)
    raiz2 = buscar(padres, nodo2)

    if raiz1 == raiz2:
        return False

    if rangos[raiz1] < rangos[raiz2]:
        padres[raiz1] = raiz2

    elif rangos[raiz1] > rangos[raiz2]:
        padres[raiz2] = raiz1

    else:
        padres[raiz2] = raiz1
        rangos[raiz1] += 1

    return True


def kruskal(nodos, conexiones):
    conexiones.sort(key=lambda conexion: conexion[2])

    padres = {}
    rangos = {}

    for nodo in nodos:
        padres[nodo] = nodo
        rangos[nodo] = 0

    arbol = []
    peso_total = 0

    for origen, destino, peso in conexiones:

        if unir(padres, rangos, origen, destino):
            arbol.append((origen, destino, peso))
            peso_total += peso

            if len(arbol) == len(nodos) - 1:
                break

    return arbol, peso_total


nodos = []

cantidad = int(input("Ingrese la cantidad de nodos: "))

for i in range(cantidad):
    nodo = input(f"Nombre del nodo {i + 1}: ")
    nodos.append(nodo)


conexiones = []

cantidad_conexiones = int(input("\nIngrese la cantidad de conexiones: "))

for i in range(cantidad_conexiones):
    print(f"\nConexion {i + 1}")

    origen = input("Nodo de origen: ")
    destino = input("Nodo de destino: ")
    peso = int(input("Peso de la conexion: "))

    conexiones.append((origen, destino, peso))


arbol, peso_total = kruskal(nodos, conexiones)

print("\n===== ARBOL DE EXPANSION MINIMA =====")

if len(arbol) != cantidad - 1:
    print("El grafo no esta conectado.")
    print("No existe un arbol de expansion minima que conecte todos los nodos.")
else:
    for origen, destino, peso in arbol:
        print(f"{origen} -- {destino} | Peso: {peso}")

    print(f"\nPeso total minimo: {peso_total}")
