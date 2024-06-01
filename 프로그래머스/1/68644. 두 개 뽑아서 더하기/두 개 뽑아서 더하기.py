from itertools import combinations

def solution(numbers):
    answer = set()
    for x, y in combinations(numbers, 2):
        answer.add(x + y)
    
    return sorted(answer)