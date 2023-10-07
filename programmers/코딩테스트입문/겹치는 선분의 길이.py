def solution(lines):
    answer = 0
    lines.sort(key=lambda x: x[0])
    times = 0
    sequence = 0
    if lines[0][1] == lines[1][0] and lines[1][1] == lines[2][0] and lines[1][1] - lines[1][0] == 1:
        answer -= 1
    for i in range(-100, 102):
        for x, y in lines:
            if x <= i and i <= y:
                times += 1
        if times >= 2:
            sequence += 1
            times = 0
        else:
            if sequence > 1:
                answer += sequence - 1
            times = 0
            sequence = 0
    return answer

lines = [[1, 2], [2, 3], [3, 4]]
print(solution(lines))
