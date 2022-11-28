import sys

input = sys.stdin.readline


def solution(numbers):
    for i in ["0", "1"]:
        if all_is_one(numbers, i):
            return i
    standard = len(numbers) // 2
    cutting_index = [0, standard]
    result = "("
    for i in cutting_index:
        for j in cutting_index:
            result += solution(cut_arrays(numbers, i, j))
    return result + ")"


def all_is_one(numbers, number):
    for i in numbers:
        for j in i:
            if j != number:
                return False
    return True


def cut_arrays(numbers, start_row, start_column):
    new_numbers = []
    standard = len(numbers) // 2
    for i in numbers[start_row:start_row + standard]:
        new_numbers.append(i[start_column:start_column + standard])
    return new_numbers


N = int(input())
array = []
for _ in range(N):
    array.append(list(map(str, input().strip())))
print(solution(array))
