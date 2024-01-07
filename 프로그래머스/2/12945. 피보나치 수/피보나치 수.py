def solution(n):
    
    a = []
    
    for i in range(0, n + 1):
        
        if i==0:
            a.append(0)
        
        elif i==1:
            a.append(1)
        
        else:
            a.append(a[-1] + a[-2])
            
    return a[-1]%1234567