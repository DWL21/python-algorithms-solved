A = ' ' + input()
B = ' ' + input()
dp = [[0] * len(B) for _ in range(len(A))]
histories = [[0] * len(B) for _ in range(len(A))] 
for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            histories[i][j] = 2
        elif dp[i - 1][j] > dp[i][j - 1]:
            dp[i][j] = dp[i - 1][j]
            histories[i][j] = 3
        else:
            dp[i][j] = dp[i][j - 1]
            histories[i][j] = 1
answer = dp[len(A) - 1][len(B) - 1]
print(answer)
if answer:
    i = len(A) - 1
    j = len(B) - 1
    sentence = []
    while histories[i][j] and i > 0 and j > 0:
        if histories[i][j] == 2:
            sentence.append(A[i])
            i -= 1
            j -= 1
        elif histories[i][j] == 1:
            j -= 1
        else:
            i -= 1
    sentence.reverse()
    print(''.join(map(str, sentence)))
