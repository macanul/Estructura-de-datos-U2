class Cola:
    """Cola (FIFO): el primero en entrar es el primero en salir."""

    def __init__(self):
        self._items = []

    def encolar(self, elemento):
        self._items.append(elemento)

    def desencolar(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        return self._items.pop(0)

    def frente(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        return self._items[0]

    def esta_vacia(self):
        return len(self._items) == 0

    def tamanio(self):
        return len(self._items)

    def __str__(self):
        return "Cola(" + ", ".join(str(x) for x in self._items) + ")"


def sumar_colas(cola_a, cola_b):
    """Recibe dos Colas de enteros y devuelve una nueva Cola con sus
    elementos sumados uno a uno. Las colas originales quedan intactas.
    Si una cola es más corta, sus posiciones faltantes cuentan como 0."""
    resultado = Cola()
    tam_a, tam_b = cola_a.tamanio(), cola_b.tamanio()

    # Se desencola, se suma y se reencola para no destruir las originales
    # (después de n vueltas cada cola recupera su orden original).
    for i in range(max(tam_a, tam_b)):
        a = 0
        b = 0
        if i < tam_a:
            a = cola_a.desencolar()
            cola_a.encolar(a)
        if i < tam_b:
            b = cola_b.desencolar()
            cola_b.encolar(b)
        resultado.encolar(a + b)
    return resultado


def crear_cola(valores):
    c = Cola()
    for v in valores:
        c.encolar(v)
    return c


def mostrar_tabla(a, b, r):
    copia_a, copia_b, copia_r = Cola(), Cola(), Cola()
    for origen, copia in ((a, copia_a), (b, copia_b), (r, copia_r)):
        for _ in range(origen.tamanio()):
            x = origen.desencolar()
            origen.encolar(x)
            copia.encolar(x)

    print(f"{'Cola A':>8} {'Cola B':>8} {'Resultado':>10}")
    while not copia_r.esta_vacia():
        va = copia_a.desencolar() if not copia_a.esta_vacia() else "-"
        vb = copia_b.desencolar() if not copia_b.esta_vacia() else "-"
        vr = copia_r.desencolar()
        print(f"{va:>8} {vb:>8} {vr:>10}")


if __name__ == "__main__":
    cola_a = crear_cola([3, 4, 2, 8, 12])
    cola_b = crear_cola([6, 2, 9, 11, 3])
    resultado = sumar_colas(cola_a, cola_b)
    mostrar_tabla(cola_a, cola_b, resultado)