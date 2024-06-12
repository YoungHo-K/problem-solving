from collections import deque


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)
        for length in range(1, len(s) + 1):
            substring = s[:length]

            for word in wordDict:
                word_length = len(word)

                if substring[-word_length:] == word:
                    dp[length] = dp[length] or dp[length - word_length]
        
        return dp[-1]
