
from abc import ABC, abstractmethod


class Node:
    """Nodo de una lista enlazada simple.

    Tiene dos referencias:
      - info: el objeto que realmente guarda el nodo.
      - next: el siguiente nodo de la lista (None si es el último).
    """

    def __init__(self, info=None, next=None):
        self.info = info
        self.next = next

    def get_info(self):
        return self.info

    def set_info(self, info):
        self.info = info

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


# ----------------------------------------------------------------------
# Order: pedido de un cliente
# ----------------------------------------------------------------------
class Order:
    """Representa un pedido: cliente y cantidad de producto."""

    def __init__(self, qtty, customer):
        self.__customer = customer
        self.__qtty = qtty

    def print(self):
        print("     Customer: " + str(self.get_customer()))
        print("     Quantity: " + str(self.get_qtty()))
        print("     ------------")

    def get_qtty(self):
        return self.__qtty

    def get_customer(self):
        return self.__customer

class QueueInterface(ABC):
    """Interfaz de una cola (estructura FIFO: First In First Out)."""

    @abstractmethod
    def size(self):
        """Devuelve el número de elementos de la cola."""

    @abstractmethod
    def is_empty(self):
        """True si la cola está vacía, False en caso contrario."""

    @abstractmethod
    def front(self):
        """Devuelve el primer elemento SIN extraerlo. None si está vacía."""

    @abstractmethod
    def enqueue(self, info):
        """Añade un nuevo elemento al final de la cola."""

    @abstractmethod
    def dequeue(self):
        """Devuelve el primer elemento Y lo extrae. None si está vacía."""


class Queue(QueueInterface):
    """Cola implementada con una lista enlazada.

    Atributos:
      top:  referencia al primer nodo (cabeza); por aquí se extraen los elementos.
      tail: referencia al último nodo; por aquí se insertan los elementos.
    Mantener tail evita recorrer toda la lista en cada inserción.
    """

    def __init__(self):
        self.top = None
        self.tail = None
        self.__size = 0

    def size(self):
        return self.__size

    def is_empty(self):
        return self.top is None

    def front(self):
        if self.is_empty():
            return None
        return self.top.get_info()

    def enqueue(self, info):
        new_node = Node(info)
        if self.is_empty():
            # Cola vacía: el nuevo nodo es a la vez cabeza y final.
            self.top = new_node
        else:
            # Se enlaza a continuación del último nodo.
            self.tail.set_next(new_node)
        self.tail = new_node
        self.__size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        info = self.top.get_info()
        # Se desenlaza el nodo de la cabeza.
        self.top = self.top.get_next()
        if self.top is None:
            # La cola quedó vacía: tail no debe seguir apuntando al nodo borrado.
            self.tail = None
        self.__size -= 1
        return info

    def print_info(self):
        """Presenta en consola el tamaño y cada elemento (usa Order.print)."""
        print("********* QUEUE DUMP *********")
        print("   Size: " + str(self.__size))
        node = self.top
        i = 1
        while node is not None:
            print("   ** Element " + str(i))
            node.get_info().print()
            node = node.get_next()
            i += 1
        print("******************************")

    def get_nth(self, pos):
        """Devuelve el n-ésimo elemento (1 = primero) sin borrarlo.

        Devuelve None si la posición no es válida.
        """
        if pos < 1 or pos > self.__size:
            return None
        node = self.top
        for _ in range(pos - 1):
            node = node.get_next()
        return node.get_info()


# En el diagrama de la guía la clase aparece como LinkedQueue.
LinkedQueue = Queue

def main():
    queue = Queue()

    # Cola vacía
    print(">>> Cola recién creada")
    queue.print_info()
    print("is_empty:", queue.is_empty())
    print("front:", queue.front())
    print("dequeue:", queue.dequeue())

    # Se crean al menos 3 pedidos y se encolan, volcando la cola tras cada operación
    o1 = Order(20, "cust1")
    o2 = Order(30, "cust2")
    o3 = Order(40, "cust3")
    o4 = Order(50, "cust3")

    for i, order in enumerate([o1, o2, o3], start=1):
        print("\n>>> enqueue pedido %d" % i)
        queue.enqueue(order)
        queue.print_info()

    # front: devuelve el primero sin extraerlo
    print("\n>>> front (no extrae)")
    queue.front().print()
    queue.print_info()

    # dequeue: devuelve el primero y lo extrae
    print("\n>>> dequeue (extrae)")
    queue.dequeue().print()
    queue.print_info()

    # Se vuelven a introducir elementos hasta tener cuatro
    print("\n>>> enqueue de dos pedidos más (la cola pasa a tener 4)")
    queue.enqueue(o1)
    queue.enqueue(o4)
    queue.print_info()

    # get_nth: obtener el tercero, y casos de posición no válida
    print("\n>>> get_nth(3)")
    queue.get_nth(3).print()
    print("get_nth(0):", queue.get_nth(0))
    print("get_nth(5):", queue.get_nth(5))
    queue.print_info()  # get_nth no borra nada

    # Se vacía la cola
    print("\n>>> Vaciando la cola")
    while not queue.is_empty():
        queue.dequeue()
        queue.print_info()
    print("dequeue en cola vacía:", queue.dequeue())


if __name__ == "__main__":
    main()