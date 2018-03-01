import math
import numpy as np


def distance(a, b, x, y):
    return int(math.fabs(a - x) + math.fabs(b - y))


example = np.genfromtxt('a_example.in', dtype='int')
should_be_easy = np.genfromtxt('b_should_be_easy.in')
no_hurry = np.genfromtxt('c_no_hurry.in')


print(distance(1, 2, 4, 7))
print(example)
