class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        answer = [[0] * n for _ in range(n)]

        number = 1
        top, bottom, left, right = 0, n - 1, 0, n - 1 
        while number <= n ** 2:

            for index in range(left, right + 1):
                answer[top][index] = number
                number += 1
            
            top += 1
            
            for index in range(top, bottom + 1):
                answer[index][right] = number
                number += 1
                
            right -= 1
            
            if left <= right:
                for index in range(right, left - 1, -1):
                    answer[bottom][index] = number
                    number += 1
                
                bottom -= 1
            
            if top <= bottom:
                for index in range(bottom, top - 1, -1):
                    answer[index][left] = number
                    number += 1
                
                left += 1
            
        return answer
        