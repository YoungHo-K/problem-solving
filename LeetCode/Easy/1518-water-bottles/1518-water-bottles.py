class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        answer = 0
        
        drink = 0        
        while numBottles > 0:
            answer += numBottles            
            drink += numBottles
            
            numBottles = drink // numExchange
            drink = drink % numExchange
            
        return answer
