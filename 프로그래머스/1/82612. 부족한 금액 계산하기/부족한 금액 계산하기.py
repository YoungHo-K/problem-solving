def solution(price, money, count):
    return -min(0, money - int(count * (count + 1) / 2) * price)