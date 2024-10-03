class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waiting_times = []
        
        now = 1
        for arrival, t in customers:
            if now < arrival:
                now = arrival
            
            now += t
            waiting_times.append(now - arrival)
            
        return round(sum(waiting_times) / len(waiting_times), 5)
