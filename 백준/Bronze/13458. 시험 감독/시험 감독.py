

def solution(n, students, b, c):
    number_of_teachers = n

    for index in range(0, n):
        number_of_students = students[index] - b
        if number_of_students <= 0:
            continue

        number_of_teachers += number_of_students // c
        if number_of_students % c != 0:
            number_of_teachers += 1

    return number_of_teachers


if __name__ == "__main__":
    N = int(input())
    STUDENTS = list(map(int, input().split()))
    B, C = list(map(int, input().split()))

    print(solution(N, STUDENTS, B, C))
