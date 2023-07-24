class Solution:
    def myAtoi(self, s: str) -> int:        
        plus_minus = ["-", "+"]
        
        answer = list()
        for value in s:
            if value == " ":
                if (len(answer) != 0) and (answer[-1] in plus_minus):
                    break
                
                if self.is_answer(answer) is False:
                    continue
                else:
                    break
                
            if value in plus_minus:
                if self.is_answer(answer) is True:
                    break
                
                if (len(answer) > 0) and (answer[-1] in plus_minus):
                    answer = list()
                    break
                
                answer.append(value)
                continue
                    
            try:
                answer.append(str(int(value)))
            except:
                break
        
        if len(answer) == 0:
            return 0
        
        try:
            answer = "".join(answer).replace("+", "")
            answer = int(answer)
        except:
            return 0
        
        if answer < -(2 ** 31):
            answer = - (2 ** 31)
        
        if answer > 2 ** 31 - 1:
            answer = 2 ** 31 - 1
                
        return answer

    def is_answer(self, values):
        try:
            answer = int("".join(values).replace("+", ""))
        except:
            return False
        
        return True
    
    