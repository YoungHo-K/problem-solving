class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                break
                            
            elif nums[mid] < target:
                left = mid + 1
            
            else:
                right = mid - 1
                
        answer = []
        for index in range(left, right + 1):
            if nums[index] == target:
                answer.append(index)
        
        if len(answer) == 0:
            return [-1, -1]
        
        return [min(answer), max(answer)]
        