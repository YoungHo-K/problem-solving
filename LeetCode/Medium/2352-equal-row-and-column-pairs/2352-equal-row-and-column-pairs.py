class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        answer = 0
                
        for row_index in range(0, len(grid)):
            for column_index in range(0, len(grid)):                
                is_pair = True                
 
                for index in range(0, len(grid)):
                    if grid[row_index][index] != grid[index][column_index]:
                        is_pair = False
                    
                        break
                        
                answer += 1 if is_pair is True else 0
                
        return answer
                        