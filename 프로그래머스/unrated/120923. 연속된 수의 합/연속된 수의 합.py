def solution(num, total):
    result =[]
    x = int((total - sum(range(num))) / num)
    for i in range(x, x+num):
        result.append(i)
    return result

## 문제 풀이 ##
# total은 x + x+1 + x+2 + x+3... 이런식으로 이루어짐
# 위 식을 정리하면, total = num(x) + sum(num-1) 이런식으로 정리가 됨.
# 여기서 x의 값을 추출하면, x = (total-sum(num-1))n 공식이 성립함.
# 이를 코드로 환산하면, (total - sum(range(num)/n)이 됨.
