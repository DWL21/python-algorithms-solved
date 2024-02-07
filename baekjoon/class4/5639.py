import sys

sys.setrecursionlimit(int(1e9))

numbers = []
while True:
    try:
        numbers.append(int(input()))
    except:
        break

result = []

def find(numbers):
    if not numbers:
        return
    root = numbers[0]
    for i in range(1, len(numbers)):
        if root < numbers[i]:
            find(numbers[1:i])
            find(numbers[i:])
            result.append(root)
            return
    find(numbers[1:])
    result.append(root)


find(numbers)

for i in result:
    print(i)

