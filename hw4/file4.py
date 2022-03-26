numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = []

for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i != j and numbers[i] == numbers[j]:
            break
    else:
        new_list.append(numbers[i])

print(new_list)
