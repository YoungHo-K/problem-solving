def solution(n, m, section):
    answer = 1
    
    start = 0
    for index in range(1, len(section)):
        if m <= (section[index] - section[start]):
            start = index
            answer += 1
        
    return answer