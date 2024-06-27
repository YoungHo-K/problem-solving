import heapq


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        
        answer = 0
        for value in nums:
            if value - 1 not in nums_set:
                length = 0
                
                while value in nums_set:
                    value += 1
                    length += 1
                
                answer = max(answer, length)
                
        return answer
                