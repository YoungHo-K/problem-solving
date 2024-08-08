import heapq


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        costs = [(cost, index) for index, cost in enumerate(costs)]
        
        left_heap = costs[:candidates]
        right_heap = costs[-candidates:]
        heapq.heapify(left_heap)
        heapq.heapify(right_heap)
        
        n = len(costs)
        left_pivot = candidates
        right_pivot = n - candidates - 1
                
        total_cost = 0
        used = set()
        for _ in range(k):
            left_value, left_index = heapq.heappop(left_heap) if len(left_heap) > 0 else (float('inf'), -1)
            right_value, right_index = heapq.heappop(right_heap) if len(right_heap) > 0 else (float('inf'), -1)
            
            if left_value <= right_value:
                total_cost += left_value
                used.add(left_index)

                if (left_pivot < n) and (left_pivot not in used):
                    heapq.heappush(left_heap, costs[left_pivot])
                    left_pivot += 1
                
                if left_index == right_index:
                    if (right_pivot >= 0) and (right_pivot not in used):
                        heapq.heappush(right_heap, costs[right_pivot])
                        right_pivot -= 1
                else:
                    heapq.heappush(right_heap, (right_value, right_index))
            
            else:
                total_cost += right_value
                used.add(right_index)
                
                if (right_pivot >= 0) and (right_pivot not in used):
                    heapq.heappush(right_heap, costs[right_pivot])
                    right_pivot -= 1
                
                heapq.heappush(left_heap, (left_value, left_index))
                
        return total_cost
            