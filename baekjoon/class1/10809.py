from string import ascii_lowercase

S = input()
for i in ascii_lowercase:
    try:
        print(S.index(i), end= " ")
    except ValueError:
        print(-1, end=" ")
