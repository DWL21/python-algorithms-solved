def recursion(s: str, l: int, r: int, times: int):
    if l >= r:
        return 1, times
    if s[r] != s[l]:
        return 0, times
    return recursion(s, l + 1, r - 1, times + 1)


def is_palindrome(s: str):
    return recursion(s, 0, len(s) - 1, 1)


N = int(input())
for _ in range(N):
    print(" ".join(map(str, is_palindrome(input()))))

