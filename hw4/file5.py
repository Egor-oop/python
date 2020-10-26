from functools import reduce


def my_func(prev_el, el):
    return prev_el * el


numbers = [i for i in range(100, 1002, 2)]

print(reduce(my_func, numbers))
