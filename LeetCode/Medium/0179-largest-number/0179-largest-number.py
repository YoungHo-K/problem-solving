from collections import defaultdict


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        nums = list(map(str, nums))
                
        for i in range(0, n - 1):
            max_index = i
            for j in range(i + 1, n):
                if nums[max_index] + nums[j] <= nums[j] + nums[max_index]:
                    max_index = j
            
            nums[i], nums[max_index] = nums[max_index], nums[i]

        answer = nums[0]
        for num_str in nums[1:]:
            if (answer == "0") and (num_str == "0"):
                continue
                
            answer += num_str
                
        return answer
