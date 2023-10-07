def solution(score):
    score = list(map(lambda x: sum(x) / 2, score))
    rankings = []
    for i in score:
        rank = 1
        for j in score:
            if i < j:
                rank += 1
        rankings.append(rank)
    return rankings

score = [[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]
print(solution(score))