def solution(sentence):
    a = [i.capitalize() for i in sentence.split(' ')]
    result = ' '.join(a)
    return result