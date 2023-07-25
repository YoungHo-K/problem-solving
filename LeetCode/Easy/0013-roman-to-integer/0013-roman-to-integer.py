class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        sub_roman_dict = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        
        answer = 0
        for key, value in sub_roman_dict.items():
            if key in s:
                answer += value
                s = s.replace(key, "")
                
        for val in s:
            answer += roman_dict[val]
            
        return answer