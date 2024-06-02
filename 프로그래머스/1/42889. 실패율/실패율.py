from collections import defaultdict


def solution(N, stages):
    players = defaultdict(int)    
    for stage in stages:
        players[stage] += 1
    
    answer = []
    total_players = 0
    for stage in range(N + 1, 0, -1):
        total_players += players[stage]        
        if stage > N:
            continue
        
        answer.append((players[stage] / total_players if total_players else 0.0, stage))    
    
    answer.sort(key=lambda x: (-x[0], x[1]))

    
    return [x[1] for x in answer]