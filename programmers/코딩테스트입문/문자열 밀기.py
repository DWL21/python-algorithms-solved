def solution(A, B):
    if A == B:
        return 0
    A = list(A)
    cases = []
    for i in range(len(A)):
        cases.append(A[len(A) - i - 1:] + A[:len(A) - i - 1])
    cases = list(map(lambda x: ''.join(x), cases))
    if B in cases:
        return cases.index(B) + 1
    return -1