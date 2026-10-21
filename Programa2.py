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


CANTIDAD_SERVICIOS = 4


class SistemaAtencion:
    def __init__(self, cantidad_servicios):
        # Una cola por servicio: 1, 2, 3, ...
        self.colas = {n: Cola() for n in range(1, cantidad_servicios + 1)}
        self.contadores = {n: 0 for n in self.colas}  # último número entregado

    def llegada_cliente(self, servicio):
        """Entrega el siguiente número de atención del servicio."""
        self.contadores[servicio] += 1
        numero = self.contadores[servicio]
        self.colas[servicio].encolar(numero)
        esperando = self.colas[servicio].tamanio() - 1
        return numero, esperando

    def atender_cliente(self, servicio):
        """Llama al siguiente cliente de la cola; None si no hay nadie."""
        cola = self.colas[servicio]
        if cola.esta_vacia():
            return None
        return cola.desencolar()

    def estado(self):
        for n, cola in self.colas.items():
            print(f"  Servicio {n}: {cola.tamanio()} cliente(s) en espera")


def interpretar(texto):
    """Convierte 'C1', 'c 2', 'A3'... en (accion, servicio)."""
    texto = texto.strip().upper().replace(" ", "")
    if len(texto) < 2 or texto[0] not in ("C", "A") or not texto[1:].isdigit():
        return None
    return texto[0], int(texto[1:])


def mostrar_ayuda(cantidad_servicios):
    print("-" * 50)
    print("COMANDOS DISPONIBLES")
    print(f"  C + número de servicio  -> llega un cliente (ej: C1)")
    print(f"  A + número de servicio  -> atender un cliente (ej: A1)")
    print(f"  E                       -> ver clientes en espera")
    print(f"  S                       -> salir")
    print(f"Servicios válidos: del 1 al {cantidad_servicios}")
    print("-" * 50)


def main():
    sistema = SistemaAtencion(CANTIDAD_SERVICIOS)
    print("=== Aseguradora: sistema de turnos ===")
    mostrar_ayuda(CANTIDAD_SERVICIOS)

    while True:
        entrada = input("\nEscribe un comando: ").strip().upper()
        if entrada == "S":
            print("Fin del programa.")
            break
        if entrada == "E":
            sistema.estado()
            continue

        comando = interpretar(entrada)
        if comando is None:
            print("Comando no válido.")
            mostrar_ayuda(CANTIDAD_SERVICIOS)
            continue

        accion, servicio = comando
        if servicio not in sistema.colas:
            print(f"El servicio {servicio} no existe. "
                  f"Elige un servicio del 1 al {CANTIDAD_SERVICIOS}.")
            continue

        if accion == "C":
            numero, esperando = sistema.llegada_cliente(servicio)
            print(f"Servicio {servicio} - Su número de atención es: {numero} "
                  f"(personas delante: {esperando})")
        else:
            numero = sistema.atender_cliente(servicio)
            if numero is None:
                print(f"Servicio {servicio} - No hay clientes en espera.")
            else:
                print(f"Servicio {servicio} - Llamando al número: {numero}")


if __name__ == "__main__":
    main()