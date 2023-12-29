def solution(a):
    return a.replace(a[0:-4], '*' * len(a[0:-4]))