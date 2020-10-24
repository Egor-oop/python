def my_func(arg_one, arg_two, arg_three):
    numbers_list = [arg_one, arg_two, arg_three]

    min_num = min(numbers_list)

    if numbers_list[0] == min_num:
        del numbers_list[0]
    elif numbers_list[1] == min_num:
        del numbers_list[1]
    elif numbers_list[2] == min_num:
        del numbers_list[2]

    max_num_first = max(numbers_list)

    if numbers_list[0] == max_num_first:
        del numbers_list[0]
    elif numbers_list[1] == max_num_first:
        del numbers_list[1]

    max_num_second = max(numbers_list)

    if numbers_list[0] == max_num_second:
        del numbers_list[0]

    print(max_num_first + max_num_second)


my_func(1, 2, 3)
