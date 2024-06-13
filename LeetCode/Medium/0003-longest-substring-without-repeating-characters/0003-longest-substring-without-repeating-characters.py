
from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0

        left = 0
        history = deque([])
        for right in range(0, len(s)):
            word = s[right]
            if word in history:
                while word in history:
                    history.popleft()
                    left += 1
                    
            answer = max(answer, right - left + 1)
            history.append(word)
            
        return answer            
            