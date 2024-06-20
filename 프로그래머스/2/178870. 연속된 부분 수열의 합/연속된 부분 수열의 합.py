from collections import deque


def solution(sequence, k):
    answer = None
    
    queue = deque([])
    sum_value = 0    
    length = float("inf")
    for index, value in enumerate(sequence):
        queue.append((index, value))
        sum_value += value
        
        while k < sum_value:
            sum_value -= queue.popleft()[1]
        
        if (k == sum_value) and (len(queue) < length):
            answer = [queue[0][0], queue[-1][0]]
            length = len(queue)

    return answer
            
    
