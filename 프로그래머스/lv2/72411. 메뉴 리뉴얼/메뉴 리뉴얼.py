
from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = list()
    
    for length in course:
        combs = list()
        for order in orders:
            combs += combinations(sorted(order), length)
        
        counter = Counter(combs).most_common()  # return tuples
        for string, count in counter:
            if (count > 1) and (count == counter[0][1]):
                answer.append("".join(string))
                continue
                
            break                
    
    return sorted(answer)
