class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        n = len(timePoints)
        
        times = []
        for point in timePoints:            
            hour, minute = point.split(":")
            hour, minute = int(hour), int(minute)
            
            times.append([hour, minute])
            times.append([hour + 24, minute])
            
        times.sort(key=lambda x: (x[0], x[1]))

        answer = float("inf")
        for index in range(1, len(times)):
            hour_diff = times[index][0] - times[index - 1][0]
            minute_diff = times[index][1] - times[index - 1][1]
            
            answer = min(answer, hour_diff * 60 + minute_diff)
                        
        return answer
        