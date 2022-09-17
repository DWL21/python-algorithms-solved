import sys
import collections

input = sys.stdin.readline

N = int(input())
numbers = list()
for _ in range(N):
    numbers.append(int(input()))
numbers.sort()

print(round(sum(numbers) / N))
print(numbers[N // 2])

counters = collections.Counter(numbers).most_common()
maximum = counters[0][1]
maximum_numbers = list()
for counter in counters:
    if counter[1] == maximum:
        maximum_numbers.append(counter[0])
if len(maximum_numbers) == 1:
    print(maximum_numbers[0])
else:
    print(sorted(maximum_numbers)[1])

print(numbers[-1] - numbers[0])
