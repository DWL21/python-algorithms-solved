N = int(input())
fac = 1
for i in range(1, N + 1):
    fac *= i
fac = str(fac)
count = 0
for i in fac[::-1]:
    if i == "0":
        count += 1
    else:
        break
print(count)
