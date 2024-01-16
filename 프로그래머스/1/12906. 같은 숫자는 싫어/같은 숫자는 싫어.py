def solution(arr):
    arr_list = []
    [arr_list.append(arr[i]) for i in range(len(arr)) if i == 0 or arr[i] != arr[i-1]]
    return arr_list