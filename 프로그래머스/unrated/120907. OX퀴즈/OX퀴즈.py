def is_correct_equation(equation):
    
    elements = equation.split('=')

    left_expression = elements[0].strip()
    right_expression = elements[1].strip()

    X, operator, Y = left_expression.split()
    Z = right_expression

    if operator == '+':
        return int(X) + int(Y) == int(Z)
    elif operator == '-':
        return int(X) - int(Y) == int(Z)
    else:
        return False

def solution(quiz):
    result = []

    for equation in quiz:
        is_correct = is_correct_equation(equation)
        result.append("O" if is_correct else "X")

    return result

