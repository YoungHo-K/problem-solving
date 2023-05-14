

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0

        substring = list()
        for letter in s:
            if letter not in substring:
                substring.append(letter)

                continue

            if answer < len(substring):
                answer = len(substring)

            temp_substring = list()
            while True:
                if substring[-1] != letter:
                    temp_substring.append(substring[-1])
                    substring = substring[: -1]

                    continue

                break

            substring = temp_substring[::-1] + [letter]

        if answer < len(substring):
            answer = len(substring)

        return answer            
            