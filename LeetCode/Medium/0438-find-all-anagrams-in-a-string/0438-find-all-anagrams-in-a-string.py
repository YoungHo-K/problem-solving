from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        s = list(s)
        p = list(p)
        
        letter_to_freq = [defaultdict(int) for _ in range(n + 1)]
        for index in range(1, n + 1):
            letter_to_freq[index] = letter_to_freq[index - 1].copy()
            letter_to_freq[index][ord(s[index - 1]) - ord("a")] += 1

        target_freq = defaultdict(int)            
        for index in range(0, m):
            target_freq[ord(p[index]) - ord("a")] += 1
            
        answer = []
        for i in range(0, n - m + 1):            
            is_anagram = True
            
            for j in range(0, 26):
                if (letter_to_freq[i + m][j] - letter_to_freq[i][j] - target_freq[j]) != 0:
                    is_anagram = False
                    break
            
            if is_anagram:
                answer.append(i)
            
        return answer
