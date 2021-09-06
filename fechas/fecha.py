
def crear_mes(nombre, abreviatura, cantidad_dias):
    """

    :param nombre: nombre del mes
    :param abreviatura: abreviatura del mes. ej: ENE
    :param cantidad_dias: cantidad de dias del mes
    :return str con el mensaje de creación del mes
    """

    return "Se creó el mes {}, que se abrevia {} y" \
           "contiene {} días".format(nombre, abreviatura,
                                     cantidad_dias)

