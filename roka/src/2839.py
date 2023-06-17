import sys

input = sys.stdin.readline

THREE_KG_SUGAR = 3
FIVE_KG_SUGAR = 5


def is_possible_case(n: int, five_kg_sugar_counting: int) -> bool:
    return (n-FIVE_KG_SUGAR*five_kg_sugar_counting)%THREE_KG_SUGAR == 0

def solution(n: int) -> int:
    for i in range(n//FIVE_KG_SUGAR, -1, -1):
        if is_possible_case(n, i):
            return i+(n-FIVE_KG_SUGAR*i)//THREE_KG_SUGAR
    return -1


N = int(input())
print(solution(N))
