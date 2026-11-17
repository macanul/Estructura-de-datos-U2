

def seleccion_descendente(lista):
    datos = lista[:]
    n = len(datos)
    for i in range(n - 1):
        pos_mayor = i
        for j in range(i + 1, n):
            if datos[j][1] > datos[pos_mayor][1]:
                pos_mayor = j
        datos[i], datos[pos_mayor] = datos[pos_mayor], datos[i]
    return datos


if __name__ == "__main__":
    print("=" * 55)
    print("SELECCIÓN: Ranking de ventas")
    print("=" * 55)
    ventas = [("Cuaderno", 120), ("Lápiz", 340), ("Mochila", 45),
              ("Borrador", 210), ("Calculadora", 80), ("Regla", 150)]
    ranking = seleccion_descendente(ventas)
    print(f"{'Lugar':<6}{'Producto':<14}{'Unidades':>8}")
    for lugar, (producto, unidades) in enumerate(ranking, start=1):
        print(f"{lugar:<6}{producto:<14}{unidades:>8}")