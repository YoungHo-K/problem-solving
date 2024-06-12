
from collections import defaultdict, deque


class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        
        dp = [float("inf")] * n
        def dfs(index):
            if n <= index:
                return 0
            
            if dp[index] != float("inf"):
                return dp[index]

            count = float("inf")
            char_to_freq = defaultdict(int)

            for i in range(index, n):
                char_to_freq[s[i]] += 1

                if len(set(char_to_freq.values())) == 1:
                    count = min(count, dfs(i + 1) + 1)
            
            dp[index] = count
            return count
                
        return dfs(0)
            

        
        

        