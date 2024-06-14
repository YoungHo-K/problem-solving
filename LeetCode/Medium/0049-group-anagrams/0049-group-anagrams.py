from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
                
        for string in strs:
            letters = [0] * 26                        
            for val in string:
                letters[ord(val) - ord("a")] += 1
                
            anagram_dict[tuple(letters)].append(string)
            
            
        return list(anagram_dict.values())
            