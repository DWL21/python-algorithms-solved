from collections import deque


def find_walls(maze: list) -> list:
    walls = []
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == 0:
                walls.append((i, j))
    return walls
               

def load_weights(walls: list) -> list:
    weight = [[0] * m for _ in range(n)]
    for x, y in walls:
        weight[x][y] = 10**6
    return weight


def load_visited(walls: list) -> list:
    visited = [[False] * m for _ in range(n)]
    for x, y in walls:
        visited[x][y] = True
    return visited
 

def find_starting(maze: list) -> tuple:
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == 2:
                return (i, j)


def inside_of_maze(x: int, y: int, size: tuple) -> bool:
    return 0 <= x and x < size[0] and 0 <= y and y < size[1]
 
         
def find_routes(base_index: tuple, size: tuple) -> list:
    x, y = base_index
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    routes = []
    for i, j in directions:
        row_index = x + i
        column_index = y + j
        if inside_of_maze(row_index, column_index, size):
            routes.append((row_index, column_index))
    return routes
   
    
def find_min_weight(weight: list, routes: list, visited: list) -> int:
    candidates = []
    for x, y in routes:
        if visited[x][y]:
            candidates.append(weight[x][y])
    return min(candidates) + 1


def process_unvisited_points(weight: list, visited: list):
    for x, i in enumerate(visited):
        for y, visiting in enumerate(i):
            if not visiting:
                weight[x][y] = -1

            
def process_starting_point(weight: list, starting: tuple):
    weight[starting[0]][starting[1]] = 0


def process_wall_points(weight: list, walls: list):
    for x, y in walls:
        weight[x][y] = 0
    
    
def solution(n: int, m: int, maze: list) -> list:
    walls = find_walls(maze)
    weight = load_weights(walls)
    visited = load_visited(walls)
    starting = find_starting(maze)
    queue = deque()
    queue.extend(find_routes(starting, (n, m)))
    visited[starting[0]][starting[1]] = True
    while queue:
        x, y = queue.popleft()
        if visited[x][y]:
            continue
        visited[x][y] = True
        routes = find_routes((x, y), (n, m))
        queue.extend(routes)
        weight[x][y] = find_min_weight(weight, routes, visited)
    process_unvisited_points(weight, visited)
    process_wall_points(weight, walls)
    process_starting_point(weight, starting)
    return weight

n, m = map(int, input().split())

maze = []
for _ in range(n):
    maze.append(list(map(int, input().split())))
for i in solution(n, m, maze):
        print(" ".join(map(str, i)))

