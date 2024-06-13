class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        
        dp = [True] * n
        dp[0] = False
        
        for num in range(2, int(n ** 0.5) + 1):
            if dp[num - 1] is True:
                i = 2
                while num * i <= n:
                    dp[num * i - 1] = False
                    i += 1
               
        answer = 0
        for is_prime in dp[:-1]:
            if is_prime:
                answer += 1
                        
        return answer
