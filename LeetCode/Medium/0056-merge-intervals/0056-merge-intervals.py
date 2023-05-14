

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        answer = list()
        x, y = intervals[0]
        for index in range(1, len(intervals)):
            next_x, next_y = intervals[index]

            if next_x <= y:
                if y < next_y:
                    y = next_y

                continue

            answer.append([x, y])
            x = next_x
            y = next_y

        if [x, y] not in answer:
            answer.append([x, y])

        return answer           


