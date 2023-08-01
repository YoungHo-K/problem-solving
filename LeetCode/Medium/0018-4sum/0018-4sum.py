class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = list()
        for i in range(0, len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                target_value = target - nums[i] - nums[j]
                
                value_dict = dict()
                for k in range(j + 1, len(nums)):
                    if nums[k] not in value_dict.keys():
                        value_dict[target_value - nums[k]] = k
                    
                        continue
                    
                    arr = [nums[i], nums[j], nums[value_dict[nums[k]]], nums[k]]
                    arr.sort()
                    if arr not in answer:
                        answer.append(arr)

        return answer