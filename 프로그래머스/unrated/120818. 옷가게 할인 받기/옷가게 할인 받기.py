def solution(price):
    result = 0
    
    if price >= 500000:
        result = price * 0.2
    elif price >= 300000:
        result = price * 0.10
    elif price >= 100000:
        result = price * 0.05
        
    return int(price - result)