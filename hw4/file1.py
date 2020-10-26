def money():
    hours = int(input('Часов отработано: '))
    sum_in_hours = int(input('$/ч: '))
    prize = int(input('Премия: '))
    cash = hours * sum_in_hours
    return cash + prize


print(f'Твой заработок на этот раз {money() }/$')
