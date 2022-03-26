def division(arg_one, arg_two):
    if arg_one <= 0:
        print(f'arg_one = {arg_one} ERROR')
    elif arg_two <= 0:
        try:
            return print(arg_one / arg_two)
        except ZeroDivisionError:
            print('ERROR: ZeroDivisionError')
    else:
        return print(arg_one / arg_two)


division(3, 7)
