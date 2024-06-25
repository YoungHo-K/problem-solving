class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        index = -1
        
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                index = i
                break
                
        if index == -1:
            nums[:] = nums[::-1]
            return
        
        for i in range(n - 1, index, -1):
            if nums[index] < nums[i]:
                nums[i], nums[index] = nums[index], nums[i]
                break
        
        nums[index + 1: ] = nums[index + 1: ][::-1]
        
