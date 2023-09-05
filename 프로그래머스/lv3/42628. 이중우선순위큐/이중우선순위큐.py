import heapq

def solution(operations):
    heap = list()
    for op in operations:
        method, num = op.split(" ")
        
        if method == "I":
            heapq.heappush(heap, int(num))
        
        if (method == "D") and (len(heap) > 0):
            if num == "-1":
                heapq.heappop(heap)
            else:
                heap.remove(max(heap))
                heapq.heapify(heap)
    
    if len(heap) == 0:
        answer = [0, 0]
    else:
        answer = [max(heap), heapq.heappop(heap)]
    
    return answer