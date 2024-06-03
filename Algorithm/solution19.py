import math

def solution(n):
    ans = math.sqrt(n)
    if ans.is_integer():
        return int(math.pow(ans+1,2))
    else:
        return -1
