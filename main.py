import vector2.vector2 as vec


data = vec.ask_for_vector()

while data[0] != 0 or data[1] != 0:
    print("La distancia al orígen del punto ({}, {}) es: {}".format(
        data[0], data[1], vec.norm(data[0], data[1])
    ))
    data = vec.ask_for_vector()

