def solution(n, computers):
    answer = 0
    
    visited = [0] * n
    for node in range(0, n):
        if visited[node] == 1:
            continue
        
        search(node, computers, visited)
        answer += 1
    
    return answer


def search(node, computers, visited):
    stack = [node]
    while stack:
        node = stack.pop()
        visited[node] = 1
        
        for next_node, conn in enumerate(computers[node]):
            if (next_node != node) and (conn == 1) and (visited[next_node] == 0):
                stack.append(next_node)

    return