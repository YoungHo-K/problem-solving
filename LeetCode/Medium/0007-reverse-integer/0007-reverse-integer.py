

class Solution:
    def reverse(self, x: int) -> int:        
        sign = 1 if x >= 0 else -1
        number = str(x) if sign == 1 else str(x)[1: ]
        threshold = 2 ** 31

        answer = sign * int(number[::-1])        
        if (answer < -threshold) or (threshold - 1 < answer):
            return 0

        return answer
