import vector2.vector2 as vec


data = input("Ingrese un vector en 2D en formato <num>,<num>: ")
data = data.split(",")
data[0] = float(data[0].strip())
data[1] = float(data[1].strip())

while data[0] != 0 or data[1] != 0:
    print("La distancia al orígen del punto ({}, {}) es: {}".format(
        data[0], data[1], vec.norm(data[0], data[1])
    ))
    data = input("Ingrese un vector en 2D en formato <num>,<num>: ")
    data = data.split(",")
    data[0] = float(data[0].strip())
    data[1] = float(data[1].strip())

