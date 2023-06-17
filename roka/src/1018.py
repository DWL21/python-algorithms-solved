import sys

input = sys.stdin.readline

WHITE = 'W'
BLACK = "B"
CHESS_BOARD_LENGTH = 8
CHESS_BOARD_SIZE = 64

def cut_chess_board(board: list) -> list:
    chess_boards = []
    for i in range(len(board[0]) - CHESS_BOARD_LENGTH + 1):
        for j in range(len(board) - CHESS_BOARD_LENGTH + 1):
            chess_boards.append([x[i:i+CHESS_BOARD_LENGTH] for x in board[j:j+CHESS_BOARD_LENGTH]])
    return chess_boards

def count_changing_sqaures(board: list) -> int:
    sqaures = 0
    for row in board[::2]:
        sqaures += (row[::2].count(BLACK)+row[1::2].count(WHITE))
    for row in board[1::2]:
        sqaures += (row[::2].count(WHITE)+row[1::2].count(BLACK))
    return min(sqaures, CHESS_BOARD_SIZE-sqaures)

def solution(board: list) -> int:
    cases = []
    for i in cut_chess_board(board):
        cases.append(count_changing_sqaures(i))
    return min(cases)


N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(input().rstrip())
print(solution(board))
