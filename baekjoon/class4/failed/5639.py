from collections import defaultdict

numbers = []
while True:
    try:
        numbers.append(int(input()))
    except:
        break

binary_tree = dict()
root = numbers[0]

records = []
for index, now in enumerate(numbers):
    records.append(now)
    if numbers[index + 1] < now:
        binary_tree[now] = [numbers[index + 1]]
    