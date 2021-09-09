catalogo = [
{'codigo': 1221, 'desc': "Leche entera 1 litro", 'precio': 54.34},
{'codigo': 2231, 'desc': "Queso untable 200gs", 'precio': 145.34},
{'codigo': 3213, 'desc': "Harina 0000 1 kilo", 'precio': 24.32},
{'codigo': 3431, 'desc': "Detergente Biodeg.", 'precio': 80.14},
{'codigo': 5431, 'desc': "Jabon cremoso 1 unidad", 'precio': 50.00},
{'codigo': 1233, 'desc': "Arroz Integral 1 kilo", 'precio': 66.33},
{'codigo': 1589, 'desc': "Gaseosa Cola 1 Litro", 'precio': 78.65},
{'codigo': 985, 'desc': "Cerveza Rubia lata 476", 'precio': 54.00},
{'codigo': 84, 'desc': "Manteca Pack 500gs", 'precio': 124.65},
{'codigo': 155, 'desc': "Fideos Tallarin 1 kilo", 'precio': 35.23},
{'codigo': 9857, 'desc': "Jamon Cocido 200 gs", 'precio': 99.32},
{'codigo': 4756, 'desc': "Queso Dambo 200 gs", 'precio': 98.34},
{'codigo': 5661, 'desc': "Patitas de Pollo 400 gs", 'precio': 144.99},
{'codigo': 1763, 'desc': "Comida Gatos 500gs", 'precio': 86.25},
{'codigo': 1356, 'desc': "Tostaditas Light 265 gs", 'precio': 32.50},
{'codigo': 1524, 'desc': "Salchichas Super Pancho", 'precio': 95.20},
{'codigo': 7341, 'desc': "Salsa de Tomate 500 gs", 'precio': 47.90}
]


def search_product():
    code = input("Ingrese el código de producto: ")
    if not code.isdigit():
        return code
    else:
        code = int(code)
        for product in catalogo:
            if product['codigo'] == code:
                return product
    return None


def validate_quantity():
    quantity = input("Ingrese la cantidad: ")
    while not quantity.isdigit() or int(quantity) <= 0:
        quantity = input("Error. Ingrese la cantidad: ")
    return int(quantity)


def new_bill():
    bill = []
    print("Ingrese F para terminar")
    product = search_product()
    while type(product) == dict or (product != "F"):
        if type(product) == dict:
            quantity = validate_quantity()
            bill.append("({} x ${}) - {}. ${}".format(quantity, product['precio'],
                                                    product['desc'], product['precio'] * quantity))
        else:
            print("No existe el producto")
        product = search_product()

    for item in bill:
        print(item)
    return bill


def new_product():
    return 0
