

def solution(n, times, profits):
    max_profit_by_day = [0] * (n + 1)
    for index, (days, profit) in enumerate(zip(times, profits)):
        end_day = index + days
        if n < end_day:
            continue

        current_profit = max_profit_by_day[index] + profit
        for i in range(end_day, n + 1):
            max_profit_by_day[i] = max(max_profit_by_day[i], current_profit)

    return max(max_profit_by_day)


if __name__ == "__main__":
    N = int(input())
    TIMES = []
    PROFITS = []

    for _ in range(0, N):
        t, p = map(int, input().split())

        TIMES.append(t)
        PROFITS.append(p)

    print(solution(N, TIMES, PROFITS))
