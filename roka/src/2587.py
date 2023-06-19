import sys
from typing import Tuple

input = sys.stdin.readline

LENGTH_OF_NUMBERS = 5

def solution(numbers: list) -> Tuple[int, int]:
    numbers.sort()
    return (sum(numbers)//LENGTH_OF_NUMBERS, numbers[LENGTH_OF_NUMBERS//2])


numbers = []
for _ in range(LENGTH_OF_NUMBERS):
    numbers.append(int(input()))
for i in solution(numbers):
    print(i)
