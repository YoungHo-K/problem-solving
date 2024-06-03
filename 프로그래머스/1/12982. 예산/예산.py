def solution(d, budget):
    answer = 0
    
    for price in sorted(d):
        budget -= price
        if budget >= 0:
            answer += 1
        
    return answer