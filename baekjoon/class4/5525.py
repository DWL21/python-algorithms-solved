N = int(input())
M = int(input())
S = input()
standard = "IO"
times = 0
i = 0
k = 0
while i < len(S):
    if S[i:i + 2] == standard:
        if i + 2 == len(S):
            times += max(0, k - N + 1)
            break
        i += 2
        k += 1
        continue
    if S[i] == "I":
        k += 1
    times += max(0, k - N)
    i += 1
    k = 0
print(times)

