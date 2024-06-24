from collections import defaultdict, deque


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=len)
        
        n = len(words)
        dp = [0] * n
        for i in range(1, n):
            target_word = words[i]

            
            for j in range(0, i):
                current_word = words[j]                
                if len(target_word) != (len(current_word) + 1):
                    continue
                
                target = 0
                current = 0
                diff = 0
                while (current < len(current_word)) and (target < len(target_word)):
                    if target_word[target] != current_word[current]:
                        diff += 1
                        target += 1
                    
                    else:
                        target += 1
                        current += 1

                if diff <= 1:
                    dp[i] = max(dp[i], dp[j] + 1)
                    
        return max(dp) + 1
