import heapq
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)
        for value in nums:
            freq_dict[value] += 1
            
        heap = [(-value, key) for key, value in freq_dict.items()]
        heapq.heapify(heap)
        
        answer = []
        for _ in range(0, k):
            answer.append(heapq.heappop(heap)[1])
            
        return answer
