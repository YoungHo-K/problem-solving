from itertools import combinations
from collections import defaultdict


class GiftStatus:
    def __init__(self):
        self.given = defaultdict(int)
        self.received = defaultdict(int)

    @property
    def score(self):
        given = sum([value for value in self.given.values()])
        received = sum([value for value in self.received.values()])
        
        return given - received
    

def solution(friends, gifts):
    friends = {name: GiftStatus() for name in friends}

    for gift in gifts:
        a, b = gift.split(" ")
        
        friends[a].given[b] += 1
        friends[b].received[a] += 1
    
    gift_dict = defaultdict(int)
    for a, b in combinations(friends, 2):
        a_given = friends[a].given[b]
        b_given = friends[b].given[a]
        
        if a_given > b_given:
            gift_dict[a] += 1

        elif a_given < b_given:
            gift_dict[b] += 1
        
        else:
            if friends[a].score > friends[b].score:
                gift_dict[a] += 1
                
            elif friends[a].score < friends[b].score:
                gift_dict[b] += 1
    
    return max(gift_dict.values()) if len(gift_dict) > 0 else 0