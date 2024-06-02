def solution(x, n):
    answer = []
    i = x
    for _ in range(n):
        answer.append(i)
        i+=x
    return answer
