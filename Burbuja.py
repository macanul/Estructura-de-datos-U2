

def burbuja(lista):
    datos = lista[:]               
    n = len(datos)
    for i in range(n - 1):
        hubo_cambio = False
        for j in range(n - 1 - i):
            if datos[j] > datos[j + 1]:
                datos[j], datos[j + 1] = datos[j + 1], datos[j]
                hubo_cambio = True
        if not hubo_cambio:         
            break
    return datos


if __name__ == "__main__":
    print("=" * 55)
    print("BURBUJA: Calificaciones del grupo")
    print("=" * 55)
    calificaciones = [8.5, 6.0, 9.8, 7.2, 5.5, 10.0, 6.9, 8.0]
    print("Original :", calificaciones)
    ordenadas = burbuja(calificaciones)
    print("Ordenadas:", ordenadas)
    print(f"Menor: {ordenadas[0]} | Mayor: {ordenadas[-1]}")