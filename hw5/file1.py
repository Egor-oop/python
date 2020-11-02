strings = []

while True:
    line = input('Вводи слова уже ')
    if line == '':
        print(strings)
        exit()
    else:
        new_line = line + '\n'
        strings.append(new_line)

    with open("test_1.txt", "w") as file:
        file.writelines(strings)
