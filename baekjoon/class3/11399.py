N = int(input())
people = list(map(int, input().split()))
people.sort()
minimum = 0
k = len(people)
for i in people:
    minimum += i * k
    k -= 1
print(minimum)
