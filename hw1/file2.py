# Можете не проверять. Не решено!


number = int(input('Введите время в секундах: '))

if number >= 60:
    number //= 60
    print(number)
    if number >= 60:
        number //= 60
        print(number)
    else:
        print(f'{hour}:{minutes}:{}')
else:
    print(f'00:00:{number}')
