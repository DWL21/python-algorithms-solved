def solution(polynomial):
    x1_coefficient = 0
    x0_coefficient = 0
    for i in polynomial.split():
        if i[-1] == 'x':
            if len(i) == 1:
                x1_coefficient += 1
            else:
                x1_coefficient += int(i[:-1])
        if i.isdigit():
            x0_coefficient += int(i)
    if x1_coefficient == 1 and x0_coefficient > 0:
        return f'x + {x0_coefficient}'
    if x1_coefficient == 1:
        return f'x'
    if x1_coefficient > 0 and x0_coefficient > 0:
        return f'{x1_coefficient}x + {x0_coefficient}'
    if x1_coefficient > 0:
        return f'{x1_coefficient}x'
    return f'{x0_coefficient}'

polypolynomial = '3 + 7 + 10x'
print(solution(polypolynomial))