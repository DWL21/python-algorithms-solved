N = int(input())
M = int(input())
S = input()
sentence = list(map(lambda x: x == "I", S))
regex = [True, False] * N + [True]
counting = 0
length = len(regex)
for i in range(len(S) - length):
    if sentence[i:i + length] == regex:
        counting += 1
print(counting)
