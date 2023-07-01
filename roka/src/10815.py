RANGE = 10**7

M = int(input())
numbers = list(map(int, input().split()))
N = int(input())
targets = list(map(int, input().split()))

cases = ['0'] * (2*RANGE + 2)
for i in numbers:
    cases[i] = '1'
print(" ".join(list(map(lambda x: cases[x], targets))))

