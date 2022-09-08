N, M = map(int, input().split())
row = M - 7
column = N - 7
board = list()
minimum = 64
answer_chess_board = ["WBWBWBWB",
                      "BWBWBWBW",
                      "WBWBWBWB",
                      "BWBWBWBW",
                      "WBWBWBWB",
                      "BWBWBWBW",
                      "WBWBWBWB",
                      "BWBWBWBW"]
for _ in range(N):
    board.append(input())
for x in range(row):
    for y in range(column):
        current = 0
        chess_board = list()
        for i in range(8):
            chess_board.append(board[y + i][x:x + 8])
        for l in range(8):
            for m in range(8):
                if chess_board[l][m] == answer_chess_board[l][m]:
                    current += 1
        minimum = min(minimum, current, 64 - current)
print(minimum)
