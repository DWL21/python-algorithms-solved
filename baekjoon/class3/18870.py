N = int(input())
numbers = list(map(int, input().split()))
number_dict = dict()
for index, value in enumerate(sorted(set(numbers))):
    number_dict[value] = index
print(" ".join(map(lambda x: str(number_dict[x]), numbers)))
