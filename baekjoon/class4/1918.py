S = input()

PA = ['*', '/']
PB = ['+', '-']

    
stack = []
answer = []
for i in S:
    if i.isalpha():
        answer.append(i)
    elif i == '(':
        stack.append(i)
    elif i in PA:
        while stack and stack[-1] in PA:
            answer.append(stack.pop())
        stack.append(i)
    if i in PB:
        while stack and stack[-1] is not '(':
            answer.append(stack.pop())
        stack.append(i)
    elif i == ')':
        while stack and stack[-1] is not '(':
            answer.append(stack.pop())
        stack.pop()
answer.extend(stack[::-1])
print(''.join(answer))
