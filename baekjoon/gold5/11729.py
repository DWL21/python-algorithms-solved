N = int(input())

answer = []

def run(n, start, end):
    if n == 1:
        answer.append((start, end))
        return

    run(n - 1, start, 6-(start + end))
    answer.append((start, end))
    run(n - 1, 6-(start + end), end)

print(2**N - 1)
run(N, 1, 3)
for i, j in answer:
    print(i, j)
