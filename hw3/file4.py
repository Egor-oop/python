def my_func(x, y):
    if y == 0:
        return 1
    x * my_func(x, y - 1)


print(my_func(4, 3))
