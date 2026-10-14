"""Torre de Hanoi"""
import sys
import time

sys.setrecursionlimit(10000)


class TorreHanoi:
    def __init__(self, n):
        """Crea las 3 torres (A, B, C) con n discos en la torre A."""
        self.n = n
        self.torres = {"A": list(range(n, 0, -1)), "B": [], "C": []}
        self.movimientos = 0

    def mover_disco(self, origen, destino):
        """Mueve el disco superior de una torre a otra."""
        disco = self.torres[origen].pop()
        self.torres[destino].append(disco)
        self.movimientos += 1

    def resolver(self, n, origen, auxiliar, destino):
        """Algoritmo recursivo clásico de la Torre de Hanói."""
        if n == 0:
            return
        self.resolver(n - 1, origen, destino, auxiliar)
        self.mover_disco(origen, destino)
        self.resolver(n - 1, auxiliar, origen, destino)

    def resolver_contando(self, n):
        """Variante rápida: solo cuenta movimientos (sin manejar torres)."""
        if n == 0:
            return 0
        return self.resolver_contando(n - 1) + 1 + self.resolver_contando(n - 1)

    def esta_resuelto(self):
        """Verifica que todos los discos estén en la torre C."""
        return len(self.torres["C"]) == self.n


def medir(n, modo="completo"):
    juego = TorreHanoi(n)
    inicio = time.perf_counter()
    if modo == "completo":
        juego.resolver(n, "A", "B", "C")
        movs = juego.movimientos
        ok = juego.esta_resuelto()
    else:
        movs = juego.resolver_contando(n)
        ok = movs == 2 ** n - 1
    fin = time.perf_counter()
    return movs, fin - inicio, ok


if __name__ == "__main__":
    # Número de discos: se toma del argumento si existe; si no, se pregunta.
    # (Si ejecutas desde un IDE o con doble clic, no hay argumentos.)
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = int(input("¿Cuántos discos? "))
    modo = sys.argv[2] if len(sys.argv) > 2 else "completo"
    movs, t, ok = medir(n, modo)
    print(f"discos={n} modo={modo} movimientos={movs} correcto={ok} tiempo={t:.6f}s")
