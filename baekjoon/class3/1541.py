def solve(calculation: str):
    index = calculation.find("-")
    if index == -1:
        return sum(list(map(int, calculation.split("+"))))
    return sum(list(map(int, calculation[:index].split("+")))) - sum(
        list(map(int, calculation[index + 1:].replace("-", "+").split("+"))))


print(solve(input()))
