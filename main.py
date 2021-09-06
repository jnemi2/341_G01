import fechas.fecha


mes = input("Ingrese el nombre del mes: ")
abrev = input("Ingrese la abreviatura: ")
cant_dias = input("Ingrese la cantidad de días: ")
print(fechas.fecha.crear_mes(mes, abrev, cant_dias))
