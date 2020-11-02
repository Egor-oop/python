my_list = ['Geek\n', 'Brains\n', 'Top\n']

with open('test_2.txt', 'w') as f_obj:
    f_obj.writelines(my_list)

with open('test_2.txt') as f_obj:
    lines = 0
    letters = 0

    for line in f_obj:
        lines += line.count("\n")
        letters = len(line)-1
        print(f'{letters} букв на строке')

    print(f'{lines} строк')
