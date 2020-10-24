my_list = [7, 5, 3, 3, 2]
new_number = int(input())
index = 0

for item in my_list:
    if new_number <= item:
        index = my_list.index(item) + 1

my_list.insert(index, new_number)

print(f'result: {my_list}')
