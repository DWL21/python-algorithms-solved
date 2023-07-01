def is_included(source: list, target: str) -> bool:
	return target in source

N, M = map(int, input().split())
source = []
answer = 0
for _ in range(N):
	source.append(input())
for _ in range(M):
	if is_included(source, input()):
		answer += 1
print(answer)

