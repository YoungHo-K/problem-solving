import heapq


def solution(n, k, enemy):
    answer = len(enemy)
    
    saving = 0
    enemy_history = list()
    for index, num_enemy in enumerate(enemy):
        if num_enemy <= n:
            heapq.heappush(enemy_history, -num_enemy)
            n -= num_enemy
            continue
        
        if saving == k:
            answer = index
            break
        
        saving += 1        
        if len(enemy_history) > 0:
            past_max_enemy = -1 * heapq.heappop(enemy_history)
            if past_max_enemy <= num_enemy:
                heapq.heappush(enemy_history, -past_max_enemy)

            else:
                n += (past_max_enemy - num_enemy)
                heapq.heappush(enemy_history, -num_enemy)
    
    return answer