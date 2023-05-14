class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if nums.count(0) != 0:
            return 0

        number_of_negative = sum([1 for val in nums if val < 0])
        if number_of_negative % 2 == 1:
            return -1

        return 1