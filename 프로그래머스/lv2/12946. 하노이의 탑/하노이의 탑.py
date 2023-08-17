def solution(n):
    answer = list()
    move(1, 3, 2, n, answer)
    
    return answer


def move(go, to, wait, n, answer):
    if n == 1:
        answer.append([go, to])
        return
        
    move(go, wait, to, n - 1, answer)
    
    answer.append([go, to])
    
    move(wait, to, go, n - 1, answer)
    