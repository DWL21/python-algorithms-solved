from collections import deque


N, M = map(int, input().split())
trustors = list(sorted(list(map(int, input().split()))[1:]))
parties = []
for _ in range(M):
    parties.append(list(map(int, input().split()))[1:])


def solution(N, trustors, parties):
    if not trustors:
        return len(parties)
    relations = [[] for _ in range(N + 1)]
    for party in parties:
        if len(party) == N:
            return 0
        for i in party:
            relations[i].extend(party[:])
    for i, relation in enumerate(relations):
        relations[i] = sorted(list(set(relation)))
    parents = [i for i in range(N + 1)]
    standard = trustors[0]
    for i in trustors:
        parents[i] = standard
    queue = deque(trustors)
    while queue:
        person = queue.popleft()
        if parents[person] != standard:
            continue
        for i in relations[person]:
            if parents[i] != standard:
                parents[i] = standard
                queue.append(i)
    trustors = set([i for i, value in enumerate(parents) if value == standard])
    times = 0
    for i in parties:
        if not trustors & set(i):
            times += 1
    return times


print(solution(N, trustors, parties))
