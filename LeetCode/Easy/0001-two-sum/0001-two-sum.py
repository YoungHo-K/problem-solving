

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()

        answer = None
        for index, value in enumerate(nums):
            if value not in nums_dict.keys():
                nums_dict[target - value] = index

                continue

            answer = [nums_dict[value], index]

        return answer
