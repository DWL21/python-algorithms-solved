white = 0
blue = 0
N = int(input())
papers = []
for _ in range(N):
    papers.append(list(map(int, input().split())))


def square(numbers):
    global white, blue
    length = len(numbers)
    total = sum(list(map(sum, numbers)))
    if total == 0:
        white += 1
    elif total == length ** 2:
        blue += 1
    else:
        length_ = length // 2
        for x, y in [(0, 0), (0, length_), (length_, 0), (length_, length_)]:
            new = []
            for i in range(x, x + length_):
                new.append(numbers[i][y:y + length_])
            square(new)


square(papers)
print(white)
print(blue)
