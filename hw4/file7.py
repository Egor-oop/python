def fakt(arg_one):
    rez = 1
    for i in range(1, arg_one + 1):
        rez *= i
        yield rez


num = int(input("введите число\n"))
for j in fakt(num):
    print(j)
