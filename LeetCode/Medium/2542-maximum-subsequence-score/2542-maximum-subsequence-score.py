import heapq


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums_pair = [(x, y) for x, y in zip(nums1, nums2)]
        nums_pair.sort(key=lambda x: -x[1])
        
        top_k_heap = [pair[0] for pair in nums_pair[: k]]
        top_k_sum = sum(top_k_heap)
        heapq.heapify(top_k_heap)

        answer = top_k_sum * nums_pair[k - 1][1]
        for index in range(k, len(nums1)):
            top_k_sum -= heapq.heappop(top_k_heap)
            top_k_sum += nums_pair[index][0]
            
            heapq.heappush(top_k_heap, nums_pair[index][0])
            
            answer = max(answer, top_k_sum * nums_pair[index][1])
            
        return answer
        