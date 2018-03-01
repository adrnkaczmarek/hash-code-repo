import math


def distance(a, b, x, y):
    return math.fabs(a - x) + math.fabs(b - y)


print(distance(1, 2, 4, 7))
