firm = {'Black': 170, 'Smith': 210, 'Potter': 190, 'Green': 150}

try:
    f_obj = open("test_3.txt", 'w')

    for last_name, salary in firm.items():
        f_obj.write(last_name + ':' + str(salary) + "\n")
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    f_obj.close()

summ = 0
count = 0
persons = []
with open("test_3.txt", "r") as f_obj:
    for line in f_obj:
        print(line, end="")
        tokens = line.split(':')
        if int(tokens[1]) <= 200:
            persons.append(tokens[0])
        summ += int(tokens[1])
        count += 1
result = summ / count
print(f"persons: {persons}")
print(f"averate: {result}")
