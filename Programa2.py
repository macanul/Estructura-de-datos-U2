class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, sitio):
        self.elementos.append(sitio)

    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        return None

    def esta_vacia(self):
        return len(self.elementos) == 0

    def mostrar(self):
        if self.esta_vacia():
            print("El historial esta vacio")
        else:
            print("Historial de sitios visitados:")
            for sitio in reversed(self.elementos):
                print(sitio)


historial = Pila()

while True:
    print("\n--- HISTORIAL DEL NAVEGADOR ---")
    print("1. Visitar un sitio")
    print("2. Mostrar historial")
    print("3. Regresar al sitio anterior")
    print("4. Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        sitio = input("Escribe el nombre o URL del sitio: ")
        historial.apilar(sitio)
        print("Sitio guardado en el historial")

    elif opcion == "2":
        historial.mostrar()

    elif opcion == "3":
        sitio = historial.desapilar()

        if sitio is None:
            print("No hay sitios para regresar")
        elif historial.esta_vacia():
            print("Ya no hay un sitio anterior")
        else:
            print("Regresaste al sitio:", historial.elementos[-1])

    elif opcion == "4":
        print("Saliendo del programa")
        break

    else:
        print("Opcion no valida")
