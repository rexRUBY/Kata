def solution(n):
    answer = 0

    while n>0:
        print(n%10)
        answer+=n%10
        n//=10
    return answer
