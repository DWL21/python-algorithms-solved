def solution(my_string):
    total = 0
    temp = []
    for i in my_string:
        if i.isdigit():
            temp.append(i)
        elif temp:
            total += int(''.join(temp))
            temp = []
    if temp:
        total += int(''.join(temp))
    return total
