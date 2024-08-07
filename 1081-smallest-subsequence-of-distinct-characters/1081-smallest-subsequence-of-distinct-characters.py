from collections import Counter


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        counter = Counter(s)
        
        stack = []
        used = set()
        
        for value in s:
            counter[value] -= 1
            
            if value in used:
                continue
                
            while stack and (value < stack[-1]) and (counter[stack[-1]] > 0):
                removed_value = stack.pop()
                used.remove(removed_value)
            
            stack.append(value)
            used.add(value)
            
        return "".join(stack)
                