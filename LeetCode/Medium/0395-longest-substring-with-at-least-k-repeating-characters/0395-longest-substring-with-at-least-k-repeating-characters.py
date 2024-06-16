from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        def search(start, end):
            if end <= start:
                return 0
            
            substring = s[start: end]
            
            answer = None
            counter = Counter(substring)
            for index, letter in enumerate(substring):
                if counter[letter] < k:
                    left = search(start, start + index)
                    right = search(start + index + 1, end + 1)
                    
                    answer = max(left, right)
                    break        
            
            if answer is None:
                answer = len(substring)
                
            return answer
    
        return search(0, len(s))