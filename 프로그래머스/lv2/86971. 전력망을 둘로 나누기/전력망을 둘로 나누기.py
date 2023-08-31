import copy

from collections import defaultdict


def solution(n, wires):
    tree = defaultdict(list)
    for x, y in wires:
        tree[x].append(y)
        tree[y].append(x)

    answer = 101
    for x, y in wires:
        temp_tree = copy.deepcopy(tree)
        temp_tree[x].remove(y)
        temp_tree[y].remove(x)
        
        count = 0
        stack = [1]
        visited = set()
        while stack:
            node = stack.pop()
            visited.add(node)
            
            for next_node in temp_tree[node]:
                if next_node not in visited:
                    stack.append(next_node)
        
        diff = abs(n - 2 * len(visited))
        if diff < answer:
            answer = diff
                
    return answer