class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)

        def dfs(pos):
            if dp[pos] != -1:
                return dp[pos]

            length = 0
            for next_index in range(pos + 1, len(nums)):
                if nums[pos] < nums[next_index]:
                    length = max(length, dfs(next_index))

            dp[pos] = length + 1
            return dp[pos]

        answer = 0
        for index in range(0, len(nums)):
            answer = max(answer, dfs(index))

        return answer
        