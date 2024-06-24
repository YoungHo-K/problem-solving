class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        strs.sort(key=len, reverse=True)
        
        for i in range(0, len(strs)):
            is_uncommon = True
            
            for j in range(0, len(strs)):                                
                if i == j:
                    continue
                
                if self.is_subsequence(strs[i], strs[j]): 
                    is_uncommon = False
                    break
            
            if is_uncommon:
                return len(strs[i])
        
        return -1
        
    def is_subsequence(self, y, x):
        length = 0
        for x_val in x:
            if (length < len(y)) and (y[length] == x_val):
                length += 1
                
        return length == len(y)

    