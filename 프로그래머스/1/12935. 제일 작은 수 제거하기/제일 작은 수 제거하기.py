def solution(x):
    if x == 10:
        return -1
    a = min(x)
    x.remove(a)
    return x