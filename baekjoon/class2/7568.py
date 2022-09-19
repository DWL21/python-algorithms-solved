N = int(input())
people = list()
people_grade = list()
for _ in range(N):
    people.append(tuple(map(int, input().split())))
for x, y in people:
    point = 1
    for i, j in people:
        if x < i and y < j:
            point += 1
    people_grade.append(point)

print(" ".join(map(str, people_grade)))
