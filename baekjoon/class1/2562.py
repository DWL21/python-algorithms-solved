numbers = list()
for _ in range(9):
    numbers.append(int(input()))
maximum = max(numbers)
index = numbers.index(maximum) + 1

print(maximum)
print(index)
