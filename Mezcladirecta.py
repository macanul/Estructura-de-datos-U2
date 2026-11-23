def distribuir(datos, longitud):
    """Fase de distribucion: reparte bloques de 'longitud' alternando F1 y F2."""
    f1, f2 = [], []
    destino = f1
    for inicio in range(0, len(datos), longitud):
        destino.extend(datos[inicio:inicio + longitud])
        destino = f2 if destino is f1 else f1
    return f1, f2


def mezclar(f1, f2, longitud, clave):
    """Fase de mezcla: mezcla bloques de F1 y F2 de tamano 'longitud'."""
    salida = []
    i = j = 0
    while i < len(f1) or j < len(f2):
        fin_i = min(i + longitud, len(f1))
        fin_j = min(j + longitud, len(f2))
        while i < fin_i and j < fin_j:
            if clave(f1[i]) <= clave(f2[j]):
                salida.append(f1[i]); i += 1
            else:
                salida.append(f2[j]); j += 1
        salida.extend(f1[i:fin_i]); i = fin_i
        salida.extend(f2[j:fin_j]); j = fin_j
    return salida


def mezcla_directa(datos, clave=lambda x: x, verbose=False):
    datos = list(datos)
    longitud = 1
    pasada = 0
    while longitud < len(datos):
        f1, f2 = distribuir(datos, longitud)
        datos = mezclar(f1, f2, longitud, clave)
        pasada += 1
        if verbose:
            print(f"Pasada {pasada} (corridas de {longitud}): {datos}")
        longitud *= 2
    return datos


if __name__ == "__main__":
    inventario = [
        ("Teclado", 350), ("Mouse", 150), ("Monitor", 2800), ("USB 32GB", 120),
        ("Laptop", 12500), ("Cable HDMI", 90), ("Webcam", 640), ("Audifonos", 480),
    ]
    print("Inventario original:", inventario, "\n")
    ordenado = mezcla_directa(inventario, clave=lambda p: p[1], verbose=True)
    print("\nInventario ordenado por precio:")
    for nombre, precio in ordenado:
        print(f"{nombre:<12} ${precio}")