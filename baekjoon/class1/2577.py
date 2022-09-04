A = int(input())
B = int(input())
C = int(input())

result = str(A * B * C)
for i in map(str, range(10)):
    print(result.count(i))
