class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        
        stack = list()
        for value in s:
            if (len(stack) > 0) and \
               ((stack[-1] == "(") and (value == ")") or \
               (stack[-1] == "{") and (value == "}") or \
               (stack[-1] == "[") and (value == "]")):
                stack.pop()
                
                continue
            
            stack.append(value)
                
        return True if len(stack) == 0 else False
            
            