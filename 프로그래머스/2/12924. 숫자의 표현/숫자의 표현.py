def solution(n):
    result=1
    
    for i in range(1, n//2+1):
        sum = 0

        while sum < n:
            sum += i

            if sum == n:
                result += 1
                break
                
            i += 1


    return result