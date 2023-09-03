from collections import deque


def solution(priorities, location):
    queue = deque()
    for pid in range(0, len(priorities)):
        queue.append(pid)

    answer = 0
    while queue:
        pid = queue.popleft()
        if priorities[pid] < max(priorities):
            queue.append(pid)
            continue
        
        answer += 1
        priorities[pid] = -1
        if pid == location:
            break
                
    return answer