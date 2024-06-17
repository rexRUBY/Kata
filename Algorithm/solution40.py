def solution(n):
    answer = ''
    while n:
        answer += str(n%3)
        n //= 3
    answer = answer[::-1]
    
    num = 1
    res = 0
    for i in answer:
        res += num * int(i)
        num *= 3
    return res
