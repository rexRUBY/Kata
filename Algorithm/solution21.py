def solution(x):
    num = str(x)
    sum = 0
    for i in num:
        sum += int(i)
    if x % sum == 0:
        return True
    else:
        return False
