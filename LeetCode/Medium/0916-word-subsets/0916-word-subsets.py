from collections import Counter


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        words1_counter = []
        for word in words1:
            words1_counter.append(Counter(word))

        words2_counter = Counter(words2[0])
        for word in words2[1:]:
            counter = Counter(word)
            
            for key, value in counter.items():
                words2_counter[key] = max(words2_counter[key], value)
        
        answer = []
        for index, counter in enumerate(words1_counter):
            if len(words2_counter - counter) == 0:
                answer.append(words1[index])
                    
        return answer
        