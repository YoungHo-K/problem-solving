class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        
        index = 0
        while True:
            val = None
            is_common = True
            for string in strs:
                if len(string) <= index:
                    is_common = False
                    break
                
                if val is None:
                    val = string[index]
                else:
                    if val != string[index]:
                        is_common = False
                        break
                        
            if is_common is True:
                answer += val
                index += 1
            else:
                break
                
        return answer
            
                        