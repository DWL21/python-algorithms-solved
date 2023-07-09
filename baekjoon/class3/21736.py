from collections import deque

empty = 'O'
wall = 'X'
start_point = 'I'
person = 'P'
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def is_visited(point: tuple) -> bool:
    return visited[point[0]][point[1]]


def is_person(campus: list, point: tuple) -> bool:
    return campus[point[0]][point[1]] == person

 
def is_banned(campus: list, point: tuple) -> bool:
    return (point[0] < 0 or point[0] >= len(campus)) or (point[1] < 0 or point[1] >= len(campus[0])) or campus[point[0]][point[1]] == wall
    

def find_start_point(campus: list) -> tuple:
    for row, i in enumerate(campus):
        for column, status in enumerate(i):
            if status == start_point:
                return (row, column)
    raise Exception('No start point')


def find_next_points(campus: list, point: tuple) -> list:
    points = []
    for x, y in directions:
        checking_point = (point[0] + x, point[1] + y)
        if not is_banned(campus, checking_point):
            points.append(checking_point)
    return points


def change_result(people: int) -> str:
    if people == 0:
        return 'TT'
    return str(people)


N, M = map(int, input().split())
visited = [[False] * M for i in range(N)]
campus = []
for _ in range(N):
    campus.append(input())
people = 0
queue = deque()
queue.append(find_start_point(campus))
while queue:
    point = queue.popleft()
    if is_visited(point):
       continue
    visited[point[0]][point[1]] = True
    if is_person(campus, point):
        people += 1
    queue.extend(find_next_points(campus, point))
print(change_result(people))

