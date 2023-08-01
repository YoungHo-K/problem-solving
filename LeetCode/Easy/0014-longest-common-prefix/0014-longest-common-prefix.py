class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        strs.sort(key=lambda x: len(x))
        base_str = strs[0]
        
        answer = ""
        
        index = 0
        while index < len(base_str):
            is_common = True
            for s in strs[1:]:
                if base_str[index] != s[index]:
                    is_common = False
                    break
                    
            if is_common is True:
                answer += base_str[index]
                index += 1
                continue
            
            break
            
        return answer
                