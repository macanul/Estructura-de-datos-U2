def registrar_pedidos(pedidos):
    cantidad = int(input("¿Cuántos pedidos deseas registrar?: "))

    for i in range(cantidad):
        numero = input("Ingresa el número del pedido: ")

        if numero in pedidos:
            print("Ese número de pedido ya existe.")
        else:
            cliente = input("Ingresa el nombre del cliente: ")
            producto = input("Ingresa el producto solicitado: ")
            precio = float(input("Ingresa el precio del pedido: "))

            pedidos[numero] = {
                "cliente": cliente,
                "producto": producto,
                "precio": precio
            }

            print("Pedido registrado correctamente.")


def mostrar_pedidos(pedidos):
    if len(pedidos) == 0:
        print("No hay pedidos registrados.")
    else:
        print("\n--- LISTA DE PEDIDOS ---")

        for numero in pedidos:
            print("Número:", numero)
            print("Cliente:", pedidos[numero]["cliente"])
            print("Producto:", pedidos[numero]["producto"])
            print("Precio: $", pedidos[numero]["precio"])
            print("------------------------")


def busqueda_hash(pedidos):
    if len(pedidos) == 0:
        print("No hay pedidos para buscar.")
        return

    buscar = input("Ingresa el número del pedido: ")

    if buscar in pedidos:
        print("\nPedido encontrado.")
        print("Número:", buscar)
        print("Cliente:", pedidos[buscar]["cliente"])
        print("Producto:", pedidos[buscar]["producto"])
        print("Precio: $", pedidos[buscar]["precio"])
    else:
        print("No se encontró ese número de pedido.")


# PROGRAMA PRINCIPAL
pedidos = {}

while True:
    print("\n===== CAFETERÍA =====")
    print("1. Registrar pedidos")
    print("2. Mostrar pedidos")
    print("3. Buscar pedido (Hash)")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        registrar_pedidos(pedidos)

    elif opcion == "2":
        mostrar_pedidos(pedidos)

    elif opcion == "3":
        busqueda_hash(pedidos)

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida.")
