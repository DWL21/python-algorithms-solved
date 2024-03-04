import sys

input = sys.stdin.readline


G = int(input())
P = int(input())
airplanes = []
for _ in range(P):
    airplanes.append(int(input()))
gates = [False] * (G + 1)
total = 0

times = [0] * (G + 1)
for i in airplanes:
    flag = False
    if times[i]:
        start = times[i] - 1
    else:
        start = i
    for j in range(start, 0, -1):
        if not gates[j]:
            gates[j] = True
            times[i] = j
            total += 1
            flag = True
            break
    if not flag:
        break
    
print(total)
