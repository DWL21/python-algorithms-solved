N = int(input())
people = list()
people_grade = list()
answer = list()
for _ in range(N):
    people.append(tuple(map(int, input().split())))
for x, y in people:
    people_grade.append(len(list(filter(lambda p: p[0] < x and p[1] < y, people))))
for i in people_grade:
    output = len(people) - len(list(filter(lambda x: x <= i, people_grade))) + 1
    answer.append(output)
print(" ".join(map(str, answer)))
