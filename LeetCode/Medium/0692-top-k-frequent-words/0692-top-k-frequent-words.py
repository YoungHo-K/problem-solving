from collections import defaultdict


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_freq = defaultdict(int)
        for word in words:
            word_freq[word] += 1
        
        return sorted(word_freq, key=lambda x: (-word_freq[x], x))[:k]
        