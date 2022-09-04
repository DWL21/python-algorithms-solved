import collections

word = input()
letters = collections.defaultdict(int)

for i in word:
    letters[i.upper()] += 1

sorted_letters = sorted(letters.items(), key=lambda x: x[1], reverse=True)
if len(sorted_letters) > 1 and sorted_letters[0][1] == sorted_letters[1][1]:
    print("?")
else:
    print(sorted_letters[0][0])
