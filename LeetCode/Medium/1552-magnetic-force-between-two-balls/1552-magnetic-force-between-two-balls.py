class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        answer = -1
        
        left, right = 1, position[-1] - position[0]
        while left <= right:
            mid = (left + right) // 2
            
            ball_count = 1
            ball_position = position[0]
            for current in position[1:]:
                if current - ball_position >= mid:
                    ball_count += 1
                    ball_position = current
                
            if m <= ball_count:
                answer = max(answer, mid)
                left = mid + 1
            
            else:
                right = mid - 1
                            
        return answer
    