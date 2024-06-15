class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []
                
        number_to_letter = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        
        answer = []
        stack = [(value, 1) for value in number_to_letter[digits[0]]]
        while stack:
            letter, length = stack.pop()
            if length == n:
                answer.append(letter)
                continue
                
            for value in number_to_letter[digits[length]]:
                stack.append((letter + value, length + 1))
    
        return answer