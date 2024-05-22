def solution(cards1, cards2, goal):
    answer = 'Yes'
    for val in goal:
        if (len(cards1) > 0) and (val == cards1[0]):
            cards1.remove(val)
            continue
        
        if (len(cards2) > 0) and (val == cards2[0]):
            cards2.remove(val)
            continue
        
        answer = "No"
        break    
    
    return answer