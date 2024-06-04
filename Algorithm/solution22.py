def solution(a, b):
    start = min(a,b)
    end = max(a,b)
    n = end - start + 1
    return n * (start + end) // 2
