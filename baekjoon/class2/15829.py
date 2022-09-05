from string import ascii_lowercase

L = int(input())
letters = input()
r = 31
M = 1234567891
total = 0
for index, letter in enumerate(letters):
    total += (ascii_lowercase.index(letter) + 1) * r ** index
print(total % M)
