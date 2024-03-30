from collections import defaultdict


def find_root(graph, reversed_graph, length):
    for i in range(1, length + 1):
        if len(graph[i]) > 1 and not reversed_graph[i]:
            return i
    print('error')


def what_shape(start, graph):
    now = start
    while True:
        if not graph[now]:
            return 2
        if len(graph[now]) == 2:
            return 3
        now = graph[now][0]
        if now == start and len(graph[now]) == 1:
            return 1



def solution(edges):
    graph = defaultdict(list)
    reversed_graph = defaultdict(list)
    for i, j in edges:
        graph[i].append(j)
        reversed_graph[j].append(i)
    length = max(graph.keys())

    root = find_root(graph, reversed_graph, length)
    answer = [root, 0, 0, 0]
    for i in graph[root]:
        result = what_shape(i, graph)
        answer[result] += 1
    return answer


edges = [[2, 3], [4, 3], [1, 1], [2, 1]]
print(solution(edges))