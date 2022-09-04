N = int(input())
for _ in range(N):
    case = input()
    answer = 0
    sequence = 0
    for i in case:
        if i == "O":
            sequence += 1
            answer += sequence
        elif i == "X":
            sequence = 0
    print(answer)
