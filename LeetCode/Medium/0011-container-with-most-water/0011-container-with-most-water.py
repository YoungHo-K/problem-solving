

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_pivot = 0
        right_pivot = len(height) - 1
        
        answer = 0
        while left_pivot <= right_pivot:
            answer = max(answer, (right_pivot - left_pivot) * min(height[left_pivot], height[right_pivot]))
            
            if height[left_pivot] > height[right_pivot]:
                right_pivot -= 1
            else:
                left_pivot += 1
                
        return answer