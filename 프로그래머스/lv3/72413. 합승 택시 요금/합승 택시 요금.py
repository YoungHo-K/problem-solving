
from collections import defaultdict, deque


def solution(n, s, a, b, fares):
    graph = defaultdict(list)
    distance = [[float("inf")] * (n + 1) for _ in range(0, n + 1)]
    for start, end, cost in fares:
        distance[start][end] = distance[end][start] = cost
        distance[start][start] = distance[end][end] = 0
        graph[start].append(end)
        graph[end].append(start)

    for pivot in range(1, n + 1):
        visited = set()

        node = pivot
        while len(visited) < n:
            visited.add(node)
            
            for next_node in graph[node]:
                distance[pivot][next_node] = min(distance[pivot][next_node],
                                                 distance[pivot][node] + distance[node][next_node])
            
            min_cost = float("inf")
            for next_node, cost in enumerate(distance[pivot]):
                if next_node == 0:
                    continue
                    
                if (next_node not in visited) and (cost < min_cost):
                    min_cost = cost
                    node = next_node
            
            if min_cost == float("inf"):
                break
        
    answer = float("inf")
    for middle_node in range(1, n + 1):
        cost = 0
        cost += distance[s][middle_node]
        cost += distance[middle_node][a]
        cost += distance[middle_node][b]
        
        if cost < answer:
            answer = cost
    
    return answer