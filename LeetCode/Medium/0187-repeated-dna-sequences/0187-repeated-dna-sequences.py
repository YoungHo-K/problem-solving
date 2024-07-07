from collections import defaultdict


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        substring_freq = defaultdict(int)
        
        for index in range(0, n - 10 + 1):
            substring = s[index: index + 10]
            substring_freq[substring] += 1
            
        answer = []
        for key, value in substring_freq.items():
            if value > 1:
                answer.append(key)
        
        return answer
            