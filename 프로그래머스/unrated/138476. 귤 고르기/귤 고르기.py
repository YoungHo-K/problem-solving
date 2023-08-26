from collections import defaultdict


def solution(k, tangerine):
    count_dict = defaultdict(int)
    for val in tangerine:
        count_dict[val] += 1
        
    sorted_count = sorted(count_dict.values(), reverse=True)
    
    answer = 0
    for val in sorted_count:
        answer += 1
        
        k -= val
        if k <= 0:
            break
        
    return answer
