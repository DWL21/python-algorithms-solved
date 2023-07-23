N = int(input())
meetings = []
for _ in range(N):
    meetings.append(tuple(map(str, input().split())))
dancings = ["ChongChong"]
for x, y in meetings:
    if x in dancings and y not in dancings:
        dancings.append(y)
    elif x not in dancings and y in dancings:
        dancings.append(x)
print(len(dancings))

