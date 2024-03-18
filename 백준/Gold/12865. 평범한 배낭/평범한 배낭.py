
class Thing:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value


def solution(n, max_weight, things):
    knapsack = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight = things[i - 1].weight
        value = things[i - 1].value

        for j in range(1, max_weight + 1):
            if j < weight:
                knapsack[i][j] = knapsack[i - 1][j]
            else:
                knapsack[i][j] = max(knapsack[i - 1][j - weight] + value, knapsack[i - 1][j])

    return knapsack[n][max_weight]


if __name__ == "__main__":
    N, MAX_WEIGHT = list(map(int, input().split()))

    THINGS = []
    for _ in range(N):
        W, V = list(map(int, input().split()))

        THINGS.append(Thing(W, V))

    print(solution(N, MAX_WEIGHT, THINGS))

