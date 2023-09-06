
from collections import defaultdict, deque


def solution(n, vertex):
    graph = defaultdict(set)
    for start, end in vertex:
        graph[start].add(end)
        graph[end].add(start)

    dp = [None] * (n + 1)
    dp[1] = 0

    queue = deque([1])
    while queue:
        node = queue.popleft()
        
        for next_node in graph[node]:
            if dp[next_node] is None:
                dp[next_node] = dp[node] + 1
                queue.append(next_node)
    
    return dp.count(max(dp[1:]))
    