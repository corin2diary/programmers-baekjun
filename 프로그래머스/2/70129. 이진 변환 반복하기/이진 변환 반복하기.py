def solution(input_data):
    count_zero = 0
    change_count = 0

    while input_data != '1':
        count_zero += input_data.count('0')
        after_remove_len = str(len(input_data.replace('0', '')))
        int_data = int(after_remove_len)
        input_data = bin(int_data)[2:]
        change_count += 1

    data_list = [change_count, count_zero]
    return data_list