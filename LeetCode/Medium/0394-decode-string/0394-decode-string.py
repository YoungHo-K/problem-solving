class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)

        stack = []
        for index in range(0, n):
            if s[index] != "]":
                stack.append(s[index])
                continue
                
            letters = []
            while stack and stack[-1] != "[":
                letters.append(stack.pop())
                
            stack.pop()
            
            nums = []
            while stack and stack[-1].isdigit() and stack[-1] != "[":
                nums.append(stack.pop())

            target = "".join(letters[::-1]) * int("".join(nums[::-1]))                                
            stack.append(target) 
            
            index += 1
            
        return "".join(stack)
