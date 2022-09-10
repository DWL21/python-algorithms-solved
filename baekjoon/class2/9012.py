N = int(input())

for _ in range(N):
    answer = 0
    success = True
    for i in input():
        if '(' == i:
            answer += 1
        else:
            answer -= 1
        if answer < 0:
            print("NO")
            success = False
            break
    if success and answer == 0:
        print("YES")
    elif success:
        print("NO")
