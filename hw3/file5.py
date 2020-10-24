def magic_func():
    res = 0
    shell = input()

    while True:
        if shell == '&':
            break

        add_plus = shell.replace(' ', '+')

        res += eval(add_plus)

        print(res)

        shell = input()


magic_func()
