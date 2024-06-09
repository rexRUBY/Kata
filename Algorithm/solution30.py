def solution(s):
    mid = s[len(s)//2]
    if len(s) % 2== 0:
        return s[len(s)//2 -1] + mid
    else:
        return mid 
