import sys
sys.setrecursionlimit(10 ** 6)

from collections import defaultdict

global on_light


def solution(n, lighthouse):
    global on_light
    
    graph = defaultdict(set)
    for a, b in lighthouse:
        graph[a].add(b)
        graph[b].add(a)
    
    on_light = [False] * n
    dfs(graph, 1, 1)

    return on_light.count(True)
            
            
def dfs(graph, current, parent):
    global on_light
    
    for child in graph[current]:
        if child == parent:
            continue
        
        if len(graph[child]) > 1:
            dfs(graph, child, current)
        
        if (on_light[current - 1] is False) and (on_light[child - 1] is False):
            on_light[current - 1] = True        
        