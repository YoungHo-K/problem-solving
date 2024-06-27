class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n, m = len(s), len(spaces)
        
        answer = ""
        space_index = 0
        for index in range(0, n):
            value = s[index]            
            if (space_index < m) and (index == spaces[space_index]):
                value = f" {value}"
                space_index += 1
            
            answer += value
        
        return answer
