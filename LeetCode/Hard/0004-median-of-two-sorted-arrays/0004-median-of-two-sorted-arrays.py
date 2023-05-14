

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        answer_nums = nums1 + nums2
        answer_nums.sort()

        center_index = len(answer_nums) // 2
        
        if len(answer_nums) % 2 == 1:
            answer = answer_nums[center_index]

        else:
            answer = sum(answer_nums[center_index - 1: center_index + 1]) / 2

        return answer
