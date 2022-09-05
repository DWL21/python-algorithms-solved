N = int(input())

answer = 0
for i in range(N):
    k = i + 1
    construct_number = 0
    for j in str(k):
        construct_number += int(j)
    construct_number += k
    if N == construct_number:
        answer = k
        print(k)
        break
if answer == 0:
    print(0)
