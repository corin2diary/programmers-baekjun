def is_palindrome(n):
    return "yes" if str(n) == str(n)[::-1] else "no"

while True:
    num = int(input())
    if num == 0:
        break
    print(is_palindrome(num))