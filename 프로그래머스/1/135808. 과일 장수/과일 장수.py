def solution(k, m, score):
    score.sort(reverse=True)
    
    answer = 0
    for index in range(0, len(score) - m + 1, m):
        answer += score[index + m - 1] * m
    
    return answer