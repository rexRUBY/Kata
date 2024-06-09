def solution(n):
    answer = '수박'
    return answer * (n//2) + answer[:n%2]
