

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        answer = sum([1 for val in sum(grid, []) if val != 0])
        answer += sum([max(line) for line in grid])
        answer += sum([max(column_line) for column_line in zip(*grid)])

        return answer
