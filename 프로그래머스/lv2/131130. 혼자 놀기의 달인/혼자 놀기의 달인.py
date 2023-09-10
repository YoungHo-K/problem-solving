import copy


def solution(cards):
    answer = 0

    for start in range(0, len(cards)):        
        visited = [0] * len(cards)
        dfs(cards, start, visited)
        
        first_group_count = visited.count(1)
        if first_group_count == len(cards):
            continue

        next_visited = copy.deepcopy(visited)
        for next_start in range(0, len(cards)):
            if next_visited[next_start] == 1:
                continue
            
            dfs(cards, next_start, next_visited)
        
            second_group_count = next_visited.count(1)
            value = first_group_count * (second_group_count - first_group_count)
            if answer < value:
                answer = value
                
            next_visited = copy.deepcopy(visited)
        
    return answer


def dfs(cards, index, visited):
    visited[index] = 1
    next_box = cards[index]
    if visited[next_box - 1] == 1:
        return
    
    dfs(cards, next_box - 1, visited)
