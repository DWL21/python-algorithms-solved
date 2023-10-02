import sys
import copy

input = sys.stdin.readline


def play_maximum(floors, N):
    maximum_floors = copy.deepcopy(floors[0])
    for i in range(1, N):
        maximum_floors = [max(maximum_floors[:2]) + floors[i][0], max(maximum_floors) + floors[i][1], max(maximum_floors[1:]) + floors[i][2]]
    return max(maximum_floors)

def play_minimum(floors, N):
    minimum_floors = copy.deepcopy(floors[0])
    for i in range(1, N):
        minimum_floors = [min(minimum_floors[:2]) + floors[i][0], min(minimum_floors) + floors[i][1], min(minimum_floors[1:]) + floors[i][2]]
    return min(minimum_floors)

N = int(input())
floors = []
for _ in range(N):
    floors.append(tuple(map(int, input().split())))

print(f'{play_maximum(floors, N)} {play_minimum(floors, N)}')
