class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        
        answer = []
        for index in range(len(s) - 1, -1, -1):
            if s[index] != "":
                answer.append(s[index])
                
        return " ".join(answer)
    