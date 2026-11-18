# ---------------- 1. ShellSort ----------------
def shell_sort(lista):
    arr = lista[:]
    n = len(arr)
    salto = n // 2
    while salto > 0:
        for i in range(salto, n):
            temp = arr[i]
            j = i
            while j >= salto and arr[j - salto] > temp:
                arr[j] = arr[j - salto]
                j -= salto
            arr[j] = temp
        salto //= 2
    return arr


# ---------------- 2. QuickSort ----------------
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    return quick_sort(menores) + iguales + quick_sort(mayores)


# ---------------- 3. HeapSort ----------------
def heapify(arr, n, raiz):
    mayor = raiz
    izq = 2 * raiz + 1
    der = 2 * raiz + 2

    if izq < n and arr[izq] > arr[mayor]:
        mayor = izq
    if der < n and arr[der] > arr[mayor]:
        mayor = der

    if mayor != raiz:
        arr[raiz], arr[mayor] = arr[mayor], arr[raiz]
        heapify(arr, n, mayor)


def heap_sort(lista):
    arr = lista[:]
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):  # construir el montículo
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):  # sacar el mayor y mandarlo al final
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr


# ---------------- 4. Radix Sort ----------------
def counting_por_digito(arr, exp):
    n = len(arr)
    salida = [0] * n
    conteo = [0] * 10

    for num in arr:
        conteo[(num // exp) % 10] += 1
    for i in range(1, 10):
        conteo[i] += conteo[i - 1]
    for num in reversed(arr):
        indice = (num // exp) % 10
        salida[conteo[indice] - 1] = num
        conteo[indice] -= 1
    return salida


def radix_positivos(arr):
    if not arr:
        return arr
    maximo = max(arr)
    exp = 1
    while maximo // exp > 0:
        arr = counting_por_digito(arr, exp)
        exp *= 10
    return arr


def radix_sort(lista):
    positivos = radix_positivos([x for x in lista if x >= 0])
    negativos = radix_positivos([-x for x in lista if x < 0])
    return [-x for x in reversed(negativos)] + positivos


# ---------------- Entrada de datos y menú ----------------
def pedir_numeros():
    while True:
        try:
            cantidad = int(input("¿Cuántos números quieres ordenar? "))
            if cantidad <= 0:
                print("Escribe un número mayor que 0.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Escribe un número entero.")

    numeros = []
    for i in range(cantidad):
        while True:
            try:
                numeros.append(int(input(f"Número {i + 1}: ")))
                break
            except ValueError:
                print("Entrada inválida. Escribe un número entero.")
    return numeros


METODOS = {
    "1": ("ShellSort", shell_sort),
    "2": ("QuickSort", quick_sort),
    "3": ("HeapSort", heap_sort),
    "4": ("Radix Sort", radix_sort),
}


def main():
    while True:
        print("\n===== MÉTODOS DE ORDENAMIENTO =====")
        print("1. ShellSort")
        print("2. QuickSort")
        print("3. HeapSort")
        print("4. Radix Sort")
        print("5. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion in METODOS:
            nombre, funcion = METODOS[opcion]
            print(f"\nMétodo elegido: {nombre}")
            numeros = pedir_numeros()
            print("Lista original:", numeros)
            print("Lista ordenada:", funcion(numeros))
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Elige del 1 al 5.")


if __name__ == "__main__":
    main()