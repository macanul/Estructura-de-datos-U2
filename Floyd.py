
def floyd(matriz, cantidad):
    distancias = [fila[:] for fila in matriz]

    for k in range(cantidad):
        for i in range(cantidad):
            for j in range(cantidad):

                if distancias[i][k] != float('inf') and distancias[k][j] != float('inf'):

                    nueva_distancia = distancias[i][k] + distancias[k][j]

                    if nueva_distancia < distancias[i][j]:
                        distancias[i][j] = nueva_distancia

    return distancias


cantidad = int(input("Ingrese la cantidad de nodos: "))

nodos = []

for i in range(cantidad):
    nodo = input(f"Nombre del nodo {i + 1}: ")
    nodos.append(nodo)

matriz = []

print("\nIngrese la matriz de adyacencia.")
print("Utilice -1 cuando no exista una conexion.")
print("Utilice 0 para la diagonal principal.")

for i in range(cantidad):
    fila = []

    for j in range(cantidad):
        valor = int(input(f"Peso de {nodos[i]} a {nodos[j]}: "))

        if valor == -1:
            fila.append(float('inf'))
        else:
            fila.append(valor)

    matriz.append(fila)


resultado = floyd(matriz, cantidad)

print("\n===== MATRIZ DE DISTANCIAS MINIMAS =====")

print("     ", end="")

for nodo in nodos:
    print(f"{nodo:>8}", end="")

print()

for i in range(cantidad):
    print(f"{nodos[i]:>5}", end="")

    for j in range(cantidad):
        if resultado[i][j] == float('inf'):
            print(f"{'INF':>8}", end="")
        else:
            print(f"{resultado[i][j]:>8}", end="")

    print()
