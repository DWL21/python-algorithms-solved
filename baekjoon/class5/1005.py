from collections import defaultdict
from collections import deque

T = int(input())


def main():
    N, K = map(int, input().split())
    dp = [0] + list(map(int, input().split()))
    graph = defaultdict(list)
    ingraph = defaultdict(list)
    indegree = [0] * (N + 1)
    for _ in range(K):
        start, end = map(int, input().split())
        graph[start].append(end)
        ingraph[end].append(start)
        indegree[end] += 1
    W = int(input())

    q = deque()
    for i in range(1, N + 1):
        if not indegree[i]:
            q.append(i)
    
    while q:
        now = q.popleft()
        maximum = 0
        for i in ingraph[now]:
            maximum =  max(maximum, dp[i])
        dp[now] += maximum
        for i in graph[now]:
            indegree[i] -= 1
            if not indegree[i]:
                q.append(i)

    print(dp[W])


for _ in range(T):
    main()
