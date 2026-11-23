def intercalar(lista_a, lista_b, clave=lambda x: x, descendente=False):
    """Intercala dos listas ordenadas en una nueva lista ordenada."""
    resultado = []
    i = j = 0
    while i < len(lista_a) and j < len(lista_b):
        a, b = clave(lista_a[i]), clave(lista_b[j])
        toma_a = a >= b if descendente else a <= b
        if toma_a:
            resultado.append(lista_a[i])
            i += 1
        else:
            resultado.append(lista_b[j])
            j += 1
    # Se copia lo que sobre de la lista que aun no se termino
    resultado.extend(lista_a[i:])
    resultado.extend(lista_b[j:])
    return resultado


if __name__ == "__main__":
    # (nombre, calificacion) ya ordenados de mayor a menor en cada grupo
    grupo_a = [("Ana", 98), ("Luis", 90), ("Marta", 85), ("Jose", 70)]
    grupo_b = [("Sofia", 100), ("Pedro", 92), ("Diana", 80)]

    ranking = intercalar(grupo_a, grupo_b, clave=lambda x: x[1], descendente=True)

    print("Grupo A:", grupo_a)
    print("Grupo B:", grupo_b)
    print("\nRanking general:")
    for pos, (nombre, cal) in enumerate(ranking, start=1):
        print(f"{pos}. {nombre:<8} {cal}")