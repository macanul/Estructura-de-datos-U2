class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, elemento):
        self.elementos.append(elemento)

    def desapilar(self):
        return self.elementos.pop()

    def esta_vacia(self):
        return len(self.elementos) == 0


def evaluar_posfija(expresion):
    pila = Pila()

    for elemento in expresion.split():
        if elemento not in ["+", "-", "*", "/"]:
            pila.apilar(float(elemento))
        else:
            b = pila.desapilar()
            a = pila.desapilar()

            if elemento == "+":
                resultado = a + b
            elif elemento == "-":
                resultado = a - b
            elif elemento == "*":
                resultado = a * b
            else:
                resultado = a / b

            pila.apilar(resultado)

    return pila.desapilar()


def evaluar_prefija(expresion):
    pila = Pila()

    elementos = expresion.split()

    for elemento in reversed(elementos):
        if elemento not in ["+", "-", "*", "/"]:
            pila.apilar(float(elemento))
        else:
            a = pila.desapilar()
            b = pila.desapilar()

            if elemento == "+":
                resultado = a + b
            elif elemento == "-":
                resultado = a - b
            elif elemento == "*":
                resultado = a * b
            else:
                resultado = a / b

            pila.apilar(resultado)

    return pila.desapilar()


print("Evaluador de expresiones con pilas")
print("1. Notacion posfija")
print("2. Notacion prefija")

opcion = input("Elige una opcion: ")

if opcion == "1":
    expresion = input(
        "Escribe la expresion posfija, separada por espacios: "
    )
    print("Resultado:", evaluar_posfija(expresion))

elif opcion == "2":
    expresion = input(
        "Escribe la expresion prefija, separada por espacios: "
    )
    print("Resultado:", evaluar_prefija(expresion))

else:
    print("Opcion no valida")
