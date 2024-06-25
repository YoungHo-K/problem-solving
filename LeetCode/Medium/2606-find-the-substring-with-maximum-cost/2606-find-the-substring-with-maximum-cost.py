class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        n = len(s)
        char_to_cost = {}

        for char in range(97, 97 + 26):
            char_to_cost[chr(char)] = char - 97 + 1
        
        for key, value in zip(chars, vals):
            char_to_cost[key] = value

        cost_arr = [0]
        for index in range(0, n):
            cost_arr.append(char_to_cost[s[index]])
                    
        dp = [0] * (n + 1)
        for index in range(1, n + 1):
            dp[index] = max(dp[index - 1] + cost_arr[index], cost_arr[index])

        return max(0, max(dp))
