import heapq


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        times = [(times[index][0], times[index][1], index) for index in range(n)]
        times.sort(key=lambda x: x[0])   
        
        answer = None
        
        chairs = [index for index in range(n)]
        heapq.heapify(chairs)
        
        used_chairs = []        
        for arrival, leaving, friend_id in times:      
            while used_chairs:
                t, chair_no = used_chairs[0]
                if t <= arrival:
                    heapq.heappush(chairs, chair_no)
                    heapq.heappop(used_chairs)
                    continue
                
                break
            
            chair_no = heapq.heappop(chairs)
            if friend_id == targetFriend:
                answer = chair_no
                break
            
            heapq.heappush(used_chairs, (leaving, chair_no))
                        
        return answer
