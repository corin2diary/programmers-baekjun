def solution(quiz):
    
    quiz_split = []
    result = []
    
    for i in quiz:
        a = i.split("=")
        quiz_split.append(a)
    
    for i in quiz_split:
        if eval(i[0]) == int(i[1]):
            result.append('O')
        else:
            result.append('X')
            
    return result
