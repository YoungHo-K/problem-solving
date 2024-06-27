class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        palindrome = list(palindrome)
        if len(palindrome) == 1:
            return ""
        
        length = len(palindrome) // 2
        
        target = None
        for index in range(0, length):
            if palindrome[index] != "a":
                target = index
                break
                
        if target is None:
            palindrome[-1] = "b"
            
        else:
            palindrome[target] = "a"
        
        return "".join(palindrome)
                