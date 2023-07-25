class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        
        answer = None
        for value in s:
            if answer is None:
                if value.isdigit() or (value in ["-", "+"]):
                    answer = value
                else:
                    break
            
            else:
                if value.isdigit():
                    answer += value
                else:
                    break
            
        if (answer is None) or (answer in ["-", "+"]):
            return 0
        
        answer = int(answer)
        if answer < - (2 ** 31):
            answer = - (2 ** 31)
        
        if answer > 2 ** 31 - 1:
            answer = 2 ** 31 - 1

        return answer