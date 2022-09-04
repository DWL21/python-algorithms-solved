numbers = list(map(int, input().split()))
if numbers[0] == 1:
    success = True
    for i in range(8):
        if not numbers[i] == i + 1:
            print("mixed")
            success = False
            break
    if success:
        print("ascending")
elif numbers[0] == 8:
    success = True
    for i in range(7, 0, -1):
        if not numbers[7 - i] == i + 1:
            print("mixed")
            success = False
            break
    if success:
        print("descending")
else:
    print("mixed")
