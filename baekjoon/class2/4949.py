while True:
    message = input()
    if message == ".":
        break
    stack = list()
    for i in message:
        if i == "[" or i == "(":
            stack.append(i)
        elif i == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(i)
                break
    if stack:
        print("no")
    else:
        print("yes")
