def solution(num, total):
    result =[]
    x = int((total - sum(range(num))) / num)
    for i in range(x, x+num):
        result.append(i)
    return result
