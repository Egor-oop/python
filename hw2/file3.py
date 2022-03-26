mounth = int(input('Введите номер месяца: '))

mounths = {'Январь': 1, 'Февраль': 2, 'Март': 3, 'Апрель': 4, 'Май': 5, 'Июнь': 6, 'Июль': 7, 'Август': 8, 'Сентябрь': 9, 'Октябрь': 10, 'Ноябрь': 11, 'Декабрь': 12}


def get_key(dic, v):
    for key, value in dic.items():
        if value == v:
            return key


if mounth == 1:
    print(get_key(mounths, 1))
elif mounth == 2:
    print(get_key(mounths, 2))
elif mounth == 3:
    print(get_key(mounths, 3))
elif mounth == 4:
    print(get_key(mounths, 4))
elif mounth == 5:
    print(get_key(mounths, 5))
elif mounth == 6:
    print(get_key(mounths, 6))
elif mounth == 7:
    print(get_key(mounths, 7))
elif mounth == 8:
    print(get_key(mounths, 8))
elif mounth == 9:
    print(get_key(mounths, 9))
elif mounth == 10:
    print(get_key(mounths, 10))
elif mounth == 11:
    print(get_key(mounths, 11))
elif mounth == 12:
    print(get_key(mounths, 12))
else:
    print('ERROR')
