class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n, m = len(sequence), len(word)
        
        answer = 0
        for start in range(0, n - m + 1):
            current = 0            
            for index in range(start, n - m + 1, m):
                if sequence[index: index + m] == word:
                    current += 1

                else:
                    answer = max(answer, current)
                    current = 0
            
            answer = max(answer, current)
            
        return answer    