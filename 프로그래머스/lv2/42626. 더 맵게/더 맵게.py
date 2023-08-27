import heapq


def solution(scoville, K):
    heap = list()
    for s in scoville:
        heapq.heappush(heap, s)

    answer = 0
    while True:
        scov = heapq.heappop(heap)
        if K <= scov:
            break
        
        if len(heap) == 0:
            answer = -1
            break
        
        next_scov = heapq.heappop(heap)
        heapq.heappush(heap, scov + next_scov * 2)
        answer += 1
    
    return answer
