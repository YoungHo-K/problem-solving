import copy


answer = -1


def solution(n, maps):
    global answer
    answer = max(answer, max(sum(maps, [])))

    move(n, maps, 0)

    return answer


def move(n, maps, depth):
    if depth >= 5:
        return

    for direction in ["UP", "DOWN", "LEFT", "RIGHT"]:
        next_maps = copy.deepcopy(maps)
        get_next_status(n, next_maps, direction)

        move(n, next_maps, depth + 1)


def get_next_status(n, maps, direction):
    global answer

    for i in range(0, n):
        merged_values = []
        temp = None

        start = 0 if (direction == "UP") or (direction == "LEFT") else n - 1
        end = n if (direction == "UP") or (direction == "LEFT") else -1
        interval = 1 if (direction == "UP") or (direction == "LEFT") else -1
        for j in range(start, end, interval):
            num = maps[j][i] if (direction == "UP") or (direction == "DOWN") else maps[i][j]
            if (num != 0) and (temp is None):
                temp = num

            elif (num != 0) and (temp is not None):
                if temp == num:
                    merged_num = temp + num
                    merged_values.append(merged_num)

                    answer = max(merged_num, answer)
                    temp = None
                else:
                    merged_values.append(temp)
                    temp = num

        if temp is not None:
            merged_values.append(temp)

        merged_values = merged_values + [0] * (n - len(merged_values))

        for index, j in enumerate(range(start, end, interval)):
            if (direction == "UP") or (direction == "DOWN"):
                maps[j][i] = merged_values[index]
            else:
                maps[i][j] = merged_values[index]


if __name__ == "__main__":
    N = int(input())

    MAPS = []
    for _ in range(0, N):
        MAPS.append(list(map(int, input().split(" "))))

    print(solution(N, MAPS))
