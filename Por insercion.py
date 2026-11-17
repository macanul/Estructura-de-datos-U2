


def insercion(lista):
    datos = lista[:]
    for i in range(1, len(datos)):
        actual = datos[i]
        j = i - 1
        while j >= 0 and datos[j].lower() > actual.lower():
            datos[j + 1] = datos[j] 
            j -= 1
        datos[j + 1] = actual        
    return datos


if __name__ == "__main__":
    print("=" * 55)
    print("INSERCIÓN: Lista de asistencia")
    print("=" * 55)
    alumnos = ["Mariana", "Carlos", "Zoe", "Alberto", "Lucía", "Beatriz", "Diego"]
    print("Original :", alumnos)
    ordenados = insercion(alumnos)
    print("Ordenados:", ordenados)