S = input()
length = len(S)
substrings = []
for i in range(length):
	for j in range(1, length - i + 1):
		substrings.append(S[i:i + j])
print(len(set(substrings)))

