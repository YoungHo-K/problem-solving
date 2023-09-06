import copy
import heapq

from collections import deque, defaultdict


class Person:
    def __init__(self, time, duration):
        self.time = time
        self.duration = duration
    

def solution(k, n, reqs):
    queues = defaultdict(deque)
    for time, duration, ctype in reqs:
        queues[ctype - 1].append(Person(time, duration))
        
    num_mentor = [1] * k    
    temp = n - k
    while temp:
        add_mentor_ctype = None
        reduce = None
        for ctype in range(0, k):
            current_waiting = get_waiting_time(copy.deepcopy(queues[ctype]), num_mentor[ctype]) 
            next_waiting = get_waiting_time(copy.deepcopy(queues[ctype]), num_mentor[ctype] + 1)
            
            if (reduce is None) or (reduce < current_waiting - next_waiting):
                reduce = current_waiting - next_waiting
                add_mentor_ctype = ctype
                
        num_mentor[add_mentor_ctype] += 1
        temp -= 1

    answer = 0
    for ctype in range(0, k):
        answer += get_waiting_time(copy.deepcopy(queues[ctype]), num_mentor[ctype])
        
    return answer


def get_waiting_time(persons, mentor):    
    heap = list()
    while persons and mentor:
        p = persons.popleft()
        heapq.heappush(heap, p.time + p.duration)
        
        mentor -= 1
    
    waiting_time = 0
    while persons:
        p = persons.popleft()        
        current_time = heapq.heappop(heap)
                
        waiting_time += max(0, current_time - p.time)
        
        heapq.heappush(heap, max(current_time, p.time) + p.duration)
        
    return waiting_time