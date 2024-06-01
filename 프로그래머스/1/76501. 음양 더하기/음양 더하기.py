def solution(absolutes, signs):
    return sum([value * (-1 + 2 * sign) for value, sign in zip(absolutes, signs)])