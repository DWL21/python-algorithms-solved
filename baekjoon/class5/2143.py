from collections import defaultdict

T = int(input())
input()
A = list(map(int, input().split()))
input()
B = list(map(int, input().split()))

caseA = defaultdict(int)
caseB = defaultdict(int)

for i in range(1, len(A) + 1):
    total = sum(A[:i])
    caseA[total] += 1
    for j in range(i, len(A)):
        total -= A[j - i]
        total += A[j]
        caseA[total] += 1

for i in range(1, len(B) + 1):
    total = sum(B[:i])
    caseB[total] += 1
    for j in range(i, len(B)):
        total -= B[j - i]
        total += B[j]
        caseB[total] += 1
        
answer = 0
for i in caseA.keys():
    if caseB[T - i] > 0:
        answer += caseA[i] * caseB[T - i]
    else:
        del caseB[T - i]

print(answer)

print(caseA)
print(caseB)
