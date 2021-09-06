import math


def ask_for_vector():
    data = input("Ingrese un vector en 2D en formato <num>,<num>: ")
    data = data.split(",")
    data[0] = float(data[0].strip())
    data[1] = float(data[1].strip())
    return data


def norm(x, y):
    return math.sqrt(x**2 + y**2)
