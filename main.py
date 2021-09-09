import productos.productos as prod


def menu():
    print("\n1- Buscar producto\n2- Ingresar nueva factura\n3- Ingresar nuevo producto\n4- Salir\n")
    selection = input("Ingrese una opción: ")
    while (not selection.isdigit()) or int(selection) > 4 or int(selection) < 1:
        selection = input("Error. Ingrese una opción: ")
    if selection == 1:
        print(prod.search_product())
    elif selection == 2:
        prod.new_bill()
    elif selection == 3:
        prod.new_product()

    return selection


option = menu()
while option != "4":
    option = menu()
