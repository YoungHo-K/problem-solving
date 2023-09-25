
answer = 0


def solution(k, dungeons):
    global answer    
    
    dfs(k, dungeons, [])    

    return answer

def dfs(k, dungeons, visited):
    global answer
    
    for index, (a, b) in enumerate(dungeons):
        if (index not in visited) and (a <= k):
            dfs(k - b, dungeons, visited + [index])
            
    if answer < len(visited):
        answer = len(visited)
            
    