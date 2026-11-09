
def dijkstra(grafo, inicio):
    distancias = {}
    anteriores = {}
    pendientes = list(grafo.keys())

    for nodo in grafo:
        distancias[nodo] = float('inf')
        anteriores[nodo] = None

    distancias[inicio] = 0

    while pendientes:
        actual = min(pendientes, key=lambda nodo: distancias[nodo])
        pendientes.remove(actual)

        if distancias[actual] == float('inf'):
            break

        for vecino, peso in grafo[actual].items():
            nueva_distancia = distancias[actual] + peso

            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                anteriores[vecino] = actual

    return distancias, anteriores


def mostrar_camino(anteriores, inicio, destino):
    camino = []
    actual = destino

    while actual is not None:
        camino.append(actual)
        actual = anteriores[actual]

    camino.reverse()

    if camino[0] != inicio:
        return "No existe camino"

    return " -> ".join(camino)


grafo = {}

cantidad = int(input("Ingrese la cantidad de nodos: "))

for i in range(cantidad):
    nodo = input(f"Nombre del nodo {i + 1}: ")
    grafo[nodo] = {}

conexiones = int(input("\nIngrese la cantidad de conexiones: "))

for i in range(conexiones):
    print(f"\nConexion {i + 1}")
    origen = input("Nodo de origen: ")
    destino = input("Nodo de destino: ")
    peso = int(input("Peso de la conexion: "))

    grafo[origen][destino] = peso
    grafo[destino][origen] = peso

inicio = input("\nIngrese el nodo inicial: ")

distancias, anteriores = dijkstra(grafo, inicio)

print("\n===== RESULTADOS DE DIJKSTRA =====")

for nodo in grafo:
    print(f"\nDestino: {nodo}")
    print(f"Distancia minima: {distancias[nodo]}")
    print(f"Camino: {mostrar_camino(anteriores, inicio, nodo)}")
