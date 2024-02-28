

def roll_dice(dice, direction):
    if direction == 4:
        return [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]

    if direction == 3:
        return [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]

    if direction == 2:
        return [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]

    if direction == 1:
        return [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]


def move_position(n, m, position, direction):
    next_x, next_y = position

    if direction == 4:
        next_x += 1

    elif direction == 3:
        next_x -= 1

    elif direction == 2:
        next_y -= 1

    else:
        next_y += 1

    if not (0 <= next_x < n) or not (0 <= next_y < m):
        return None

    return (next_x, next_y)


def solution(n, m, position, maps, commands):
    dice = [0, 0, 0, 0, 0, 0]

    for direction in commands:
        next_position = move_position(n, m, position, direction)
        if next_position is None:
            continue

        dice = roll_dice(dice, direction)
        position = next_position

        if maps[position[0]][position[1]] == 0:
            maps[position[0]][position[1]] = dice[0]

        else:
            dice[0] = maps[position[0]][position[1]]
            maps[position[0]][position[1]] = 0

        print(dice[5])


if __name__ == "__main__":
    N, M, X, Y, K = list(map(int, input().split()))

    MAPS = []
    for _ in range(0, N):
        MAPS.append(list(map(int, input().split())))

    COMMANDS = list(map(int, input().split()))

    solution(N, M, (X, Y), MAPS, COMMANDS)
