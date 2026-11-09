
def warshall(matriz, cantidad):
    alcanzabilidad = [fila[:] for fila in matriz]

    for k in range(cantidad):
        for i in range(cantidad):
            for j in range(cantidad):

                if alcanzabilidad[i][k] == 1 and alcanzabilidad[k][j] == 1:
                    alcanzabilidad[i][j] = 1

    return alcanzabilidad


cantidad = int(input("Ingrese la cantidad de nodos: "))

nodos = []

for i in range(cantidad):
    nodo = input(f"Nombre del nodo {i + 1}: ")
    nodos.append(nodo)

matriz = []

print("\nIngrese la matriz de adyacencia.")
print("Escriba 1 si existe conexion y 0 si no existe.")

for i in range(cantidad):
    fila = []

    for j in range(cantidad):
        valor = int(input(f"Conexion de {nodos[i]} a {nodos[j]} (0 o 1): "))
        fila.append(valor)

    matriz.append(fila)


resultado = warshall(matriz, cantidad)

print("\n===== MATRIZ DE ALCANZABILIDAD =====")

print("     ", end="")

for nodo in nodos:
    print(f"{nodo:>5}", end="")

print()

for i in range(cantidad):
    print(f"{nodos[i]:>5}", end="")

    for j in range(cantidad):
        print(f"{resultado[i][j]:>5}", end="")

    print()


print("\n===== RESULTADOS =====")

for i in range(cantidad):
    for j in range(cantidad):
        if i != j:
            if resultado[i][j] == 1:
                print(f"Existe un camino de {nodos[i]} a {nodos[j]}")
            else:
                print(f"No existe un camino de {nodos[i]} a {nodos[j]}")
