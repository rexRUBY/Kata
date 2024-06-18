def solution(s):
    answer=[]
    for i in s.split(' '):
        for j in range(len(i)):
            if j % 2 == 0:
                answer.append(i[j].upper())
            else:
                answer.append(i[j].lower())
        answer.append(' ')
    return ''.join(answer[:-1])
