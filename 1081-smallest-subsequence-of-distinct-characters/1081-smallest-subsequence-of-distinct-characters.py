from collections import Counter


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        counter = Counter(s)
        
        answer = []
        for value in s:
            while answer and (value not in answer) and (value < answer[-1]) and (counter[answer[-1]] > 0):
                answer.pop()
            
            if value not in answer:
                answer.append(value)
                
            counter[value] -= 1
        
        return ''.join(answer)
        