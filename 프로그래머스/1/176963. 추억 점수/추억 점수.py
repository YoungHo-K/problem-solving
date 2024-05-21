from collections import defaultdict


def solution(name, yearning, photo):
    person_to_yearning = defaultdict(int)
    for person, score in zip(name, yearning):
        person_to_yearning[person] = score
    
    answer = []
    for persons in photo:
        answer.append(sum([person_to_yearning[person] for person in persons]))
    
    return answer