

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        answer = None
        for right_pivot in range(0, len(s) - 1, 1):
            left_pivot = right_pivot

            for index in range(left_pivot, len(s), 1):
                if s[right_pivot] != s[index]:
                    break
                
                left_pivot = index

            move = min(right_pivot, len(s) - left_pivot - 1)
            for _ in range(0, move, 1):
                if s[right_pivot - 1] != s[left_pivot + 1]:
                    break

                right_pivot -= 1
                left_pivot += 1

            subanswer = s[right_pivot: left_pivot + 1]
            if (answer is None) or (len(answer) < len(subanswer)):
                answer = subanswer

        return answer
