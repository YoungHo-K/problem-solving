import heapq


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        
        left_pivot = candidates - 1
        left_heap = costs[:candidates]
        heapq.heapify(left_heap)
        
        right_pivot = n - candidates
        right_heap = [costs[index] for index in range(right_pivot, n) if left_pivot < index]
        heapq.heapify(right_heap)
        
        total_cost = 0        
        for _ in range(k):
            left_value = left_heap[0] if len(left_heap) > 0 else float('inf')
            right_value = right_heap[0] if len(right_heap) > 0 else float('inf')
            
            if left_value <= right_value:
                total_cost += left_value
                heapq.heappop(left_heap)
                
                if left_pivot + 1 < right_pivot:
                    heapq.heappush(left_heap, costs[left_pivot + 1])
                    left_pivot += 1
                
            else:
                total_cost += right_value
                heapq.heappop(right_heap)
                
                if left_pivot < right_pivot - 1:
                    heapq.heappush(right_heap, costs[right_pivot - 1])
                    right_pivot -= 1
                    
        return total_cost
