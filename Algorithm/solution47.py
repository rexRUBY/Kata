def solution(strings, n):
    return sorted(strings, key=lambda k: (k[n], k))
