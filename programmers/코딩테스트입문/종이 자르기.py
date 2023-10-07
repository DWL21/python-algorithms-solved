def solution(M, N):
    if M < N:
        M, N = N, M
    return M - 1 + M * (N - 1)
