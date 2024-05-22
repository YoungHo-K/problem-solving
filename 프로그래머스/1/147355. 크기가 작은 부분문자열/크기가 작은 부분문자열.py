def solution(t, p):
    answer = 0
    
    for index in range(0, len(t) - len(p) + 1):
        if t[index: index + len(p)] <= p:
            answer += 1
    
    return answer