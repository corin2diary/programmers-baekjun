def solution(s):
    a = list(map(int, s.split(" ")))
    b, c = str(min(a)), str(max(a))
    return b + " " + c