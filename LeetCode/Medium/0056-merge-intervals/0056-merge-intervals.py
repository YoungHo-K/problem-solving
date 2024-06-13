

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        
        intervals.sort(key=lambda x: x[0])
        
        start = intervals[0][0]
        end = intervals[0][1]
        
        answer = []
        for index in range(1, len(intervals)):
            if start <= intervals[index][0] <= end:
                end = max(end, intervals[index][1])
                continue
            
            answer.append([start, end])
            
            start = intervals[index][0]
            end = intervals[index][1]

        answer.append([start, end])
            
        return answer
