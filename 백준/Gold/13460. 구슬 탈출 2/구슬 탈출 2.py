

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


answer = None


def solution(n, m, maps):
    global answer

    red_ball, blue_ball, goal = find_ball_and_goal_position(n, m, maps)
    move(n, m, maps, red_ball, blue_ball, goal, 1)

    return answer if answer is not None else -1


def find_ball_and_goal_position(n, m, maps):
    red_ball = None
    blue_ball = None
    goal = None

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if maps[i][j] == "R":
                red_ball = Position(i, j)

            elif maps[i][j] == "B":
                blue_ball = Position(i, j)

            elif maps[i][j] == "O":
                goal = Position(i, j)

    return red_ball, blue_ball, goal


def move(n, m, maps, red_ball, blue_ball, goal, depth):
    global answer

    if depth > 10:
        return

    for direction in ["UP", "DOWN", "LEFT", "RIGHT"]:
        next_red_ball = get_next_position(n, m, maps, red_ball, direction)
        next_blue_ball = get_next_position(n, m, maps, blue_ball, direction)
        if (next_blue_ball.x == goal.x) and (next_blue_ball.y == goal.y):
            continue

        if (next_red_ball.x == goal.x) and (next_red_ball.y == goal.y):
            answer = min(answer, depth) if answer is not None else depth
            continue

        next_red_ball, next_blue_ball = check_same_position(red_ball, next_red_ball, blue_ball, next_blue_ball, direction)

        move(n, m, maps, next_red_ball, next_blue_ball, goal, depth + 1)


def get_next_position(n, m, maps, ball, direction):
    next_x = ball.x
    next_y = ball.y

    if direction == "UP":
        for index in range(1, ball.x):
            if maps[ball.x - index][ball.y] == "O":
                next_x = ball.x - index
                break

            if maps[ball.x - index][ball.y] != "#":
                next_x = ball.x - index
                continue

            break

    elif direction == "DOWN":
        for index in range(ball.x + 1, n - 1):
            if maps[index][ball.y] == "O":
                next_x = index
                break

            if maps[index][ball.y] != "#":
                next_x = index
                continue

            break

    elif direction == "RIGHT":
        for index in range(ball.y + 1, m - 1):
            if maps[ball.x][index] == "O":
                next_y = index
                break

            if maps[ball.x][index] != "#":
                next_y = index
                continue

            break

    elif direction == "LEFT":
        for index in range(1, ball.y):
            if maps[ball.x][ball.y - index] == "O":
                next_y = ball.y - index
                break

            if maps[ball.x][ball.y - index] != "#":
                next_y = ball.y - index
                continue

            break

    return Position(next_x, next_y)


def check_same_position(red_ball, next_red_ball, blue_ball, next_blue_ball, direction):
    if direction == "UP":
        if (next_red_ball.x == next_blue_ball.x) and (red_ball.y == blue_ball.y) and (red_ball.x < blue_ball.x):
            next_blue_ball.x += 1
        elif (next_red_ball.x == next_blue_ball.x) and (red_ball.y == blue_ball.y) and (red_ball.x > blue_ball.x):
            next_red_ball.x += 1

    elif direction == "DOWN":
        if (next_red_ball.x == next_blue_ball.x) and (red_ball.y == blue_ball.y) and (red_ball.x < blue_ball.x):
            next_red_ball.x -= 1
        elif (next_red_ball.x == next_blue_ball.x) and (red_ball.y == blue_ball.y) and (red_ball.x > blue_ball.x):
            next_blue_ball.x -= 1

    elif direction == "LEFT":
        if (next_red_ball.y == next_blue_ball.y) and (red_ball.x == blue_ball.x) and (red_ball.y < blue_ball.y):
            next_blue_ball.y += 1
        elif (next_red_ball.y == next_blue_ball.y) and (red_ball.x == blue_ball.x) and (red_ball.y > blue_ball.y):
            next_red_ball.y += 1

    elif direction == "RIGHT":
        if (next_red_ball.y == next_blue_ball.y) and (red_ball.x == blue_ball.x) and (red_ball.y < blue_ball.y):
            next_red_ball.y -= 1
        elif (next_red_ball.y == next_blue_ball.y) and (red_ball.x == blue_ball.x) and (red_ball.y > blue_ball.y):
            next_blue_ball.y -= 1

    return next_red_ball, next_blue_ball


if __name__ == "__main__":
    N, M = map(int, input().split())

    MAPS = []
    for _ in range(0, N):
        MAPS.append(list(input()))

    print(solution(N, M, MAPS))
