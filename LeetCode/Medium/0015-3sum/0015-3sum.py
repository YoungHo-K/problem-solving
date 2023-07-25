class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        
        for index in range(0, len(nums) - 2):
            target_value = -nums[index]
            
            value_dict = dict()
            for next_index in range(index + 1, len(nums)):
                value = nums[next_index]
                if value in value_dict.keys():
                    arr = [-target_value, value_dict[value], value]
                    arr.sort()
                    
                    answer.add(tuple(arr))
                else:
                    value_dict[target_value - value] = value
                    
        return answer
                
