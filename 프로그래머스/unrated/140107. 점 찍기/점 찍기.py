import math


def solution(k, d):
    distance = int((d / k) ** 2)

    answer = 0
    b = 0
    while True:
        stop_val = distance - b ** 2
        if stop_val < 0:
            break
        
        answer += int(math.sqrt(stop_val)) + 1
        b += 1
    
    return answer