def corridas_naturales(datos, clave):
    """Divide la lista en tramos ya ordenados (corridas naturales)."""
    if not datos:
        return []
    corridas, actual = [], [datos[0]]
    for x in datos[1:]:
        if clave(x) >= clave(actual[-1]):
            actual.append(x)
        else:
            corridas.append(actual)
            actual = [x]
    corridas.append(actual)
    return corridas


def mezclar_dos(a, b, clave):
    salida, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        if clave(a[i]) <= clave(b[j]):
            salida.append(a[i]); i += 1
        else:
            salida.append(b[j]); j += 1
    return salida + a[i:] + b[j:]


def mezcla_equilibrada(datos, clave=lambda x: x, verbose=False):
    # Fase inicial: distribuir corridas naturales alternando en 2 cintas
    corridas = corridas_naturales(list(datos), clave)
    cinta1 = corridas[0::2]
    cinta2 = corridas[1::2]
    pasada = 0
    if verbose:
        print(f"Corridas naturales detectadas: {len(corridas)}")

    # Fases de mezcla: se mezclan corridas de las cintas de entrada y se
    # escriben alternadamente en las cintas de salida; luego se invierten roles.
    while len(cinta1) + len(cinta2) > 1:
        salida1, salida2 = [], []
        destino = salida1
        for k in range(max(len(cinta1), len(cinta2))):
            a = cinta1[k] if k < len(cinta1) else []
            b = cinta2[k] if k < len(cinta2) else []
            destino.append(mezclar_dos(a, b, clave))
            destino = salida2 if destino is salida1 else salida1
        cinta1, cinta2 = salida1, salida2  # intercambio de roles
        pasada += 1
        if verbose:
            print(f"Pasada {pasada}: cinta1={len(cinta1)} corridas, "
                  f"cinta2={len(cinta2)} corridas")

    return (cinta1 or cinta2)[0] if (cinta1 or cinta2) else []


if __name__ == "__main__":
    ventas = [520, 800, 950, 120, 300, 310, 700, 90, 400, 410, 880, 50, 60, 70]
    print("Ventas originales:", ventas, "\n")
    ordenadas = mezcla_equilibrada(ventas, verbose=True)
    print("\nVentas ordenadas:", ordenadas)
    assert ordenadas == sorted(ventas)
    print("Verificacion contra sorted(): OK")