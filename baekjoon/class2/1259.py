while True:
    N = input()
    is_palindrome = True
    if N == "0":
        break
    for i in range(len(N) // 2):
        if N[i] != N[-(i + 1)]:
            is_palindrome = False
            break
    if is_palindrome:
        print("yes")
    else:
        print("no")
