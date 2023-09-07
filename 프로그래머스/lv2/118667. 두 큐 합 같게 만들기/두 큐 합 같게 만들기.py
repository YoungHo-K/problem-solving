
from collections import deque


def solution(queue1, queue2):
    length = len(queue1)
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)
    if (sum_q1 + sum_q2) % 2 == 1:
        return -1
    
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    while (sum_q1 != sum_q2) and (queue1 and queue2) and (answer < 4 * length):
        if sum_q1 > sum_q2:
            val = queue1.popleft()
            queue2.append(val)
            
        else:
            val = queue2.popleft()
            queue1.append(val)            
            val *= -1

        answer += 1            
        sum_q1 -= val
        sum_q2 += val        
    
    if (len(queue1) == 0) or (len(queue2) == 0) or (4 * length <= answer):
        answer = -1
            
    return answer