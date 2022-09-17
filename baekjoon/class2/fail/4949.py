sentence = input()
while sentence != ".":
    success = True
    is_opened_round = False
    is_opened_square = False
    square_brackets = 0
    round_brackets = 0
    for i in sentence:
        if i == "[":
            square_brackets += 1
            is_opened_square = True
        elif i == "]":
            square_brackets -= 1
        elif i == "(":
            round_brackets += 1
            is_opened_round = True
        elif i == ")":
            round_brackets -= 1
        if (square_brackets < 0) or (round_brackets < 0):
            success = False
            print("no")
            break
        if square_brackets == 1 and not is_opened_square:
            lock_round = True
        elif round_brackets == 1 and not is_opened_square:
            lock_square = True
        if (is_opened_round and round_brackets == 0) or (is_opened_square and square_brackets == 0):
            success = False
            print("no")
            break
        if is_opened_square and square_brackets == 0:
            lock_square = False
        if is_opened_square and round_brackets == 0:
            lock_square = False

    if success:
        print("yes")
    sentence = input()
