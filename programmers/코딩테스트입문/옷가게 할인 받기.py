STANDARD = 10**5


def solution(price):
    if price >= STANDARD * 5:
        return int(price * 0.8)
    if price >= STANDARD * 3:
        return int(price * 0.9)
    if price >= STANDARD:
        return int(price * 0.95)
    return price
