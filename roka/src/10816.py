RANGE = 10**7

N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

number_counter = [0] * (RANGE*2 + 2)
for i in numbers:
	number_counter[i] += 1 
print(" ".join(map(lambda x: str(number_counter[x]), targets)))


