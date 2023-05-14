

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        answer = [""] * (1000 * numRows)

        x_pos, y_pos = 0, 0
        index = 0
        while index < len(s):
            position = x_pos * 1000 + y_pos
            answer[position] = s[index]

            if x_pos == numRows - 1:
                while (x_pos > 0) and (index < len(s) - 1):
                    x_pos -= 1
                    y_pos += 1
                    index += 1

                    position = x_pos * 1000 + y_pos
                    answer[position] = s[index]

            if numRows > 1:
                x_pos += 1
            
            else:
                y_pos += 1

            index += 1

        answer = "".join(answer)

        return answer
