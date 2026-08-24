import math

def square(side):
    side = math.ceil(side)
    return side*side

side = float(input("Введите длину стороны квадрата: "))
print(square(side))