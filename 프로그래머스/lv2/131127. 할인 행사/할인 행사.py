
from collections import deque, defaultdict


def solution(want, number, discount):
    answer = 0
    history = deque()
    continuous = {key: False for key in want}
    count_check = defaultdict(int)
    for item in discount[:10]:
        history.append(item)        
        if item not in want:
            continue
            
        count_check[item] += 1
        if number[want.index(item)] <= count_check[item]:
            continuous[item] = True
        
    if all(continuous.values()) is True:
        answer += 1
            
    for item in discount[10:]:
        past_item = history.popleft()   
        if past_item in want:
            count_check[past_item] = max(0, count_check[past_item] - 1)
            if count_check[past_item] < number[want.index(past_item)]:
                continuous[past_item] = False

        history.append(item)                
        
        if item in want:                
            count_check[item] += 1
            if number[want.index(item)] <= count_check[item]:
                continuous[item] = True
        
        if all(continuous.values()) is True:
            answer += 1
                
    return answer
