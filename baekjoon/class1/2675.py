T = int(input())
for _ in range(T):
    R, S = map(str, input().split())
    answer = ""
    for i in S:
        answer += i * int(R)
    print(answer)
