from collections import defaultdict


def solution(survey, choices):
    metrics = [["R", "T"], ["C", "F"], ["J", "M"], ["A", "N"]]
    choice_to_score = {1: 3, 2: 2, 3: 1, 4: 0, 5:1, 6: 2, 7: 3}

    metric_score = defaultdict(int)   
    for s, choice in zip(survey, choices):
        index = 1 if 5 <= choice else 0
        
        metric_score[s[index]] += choice_to_score[choice]
        
    answer = ''
    for i, j in metrics:
        if metric_score[i] >= metric_score[j]:
            answer += i
        
        else:
            answer += j
    
    return answer
