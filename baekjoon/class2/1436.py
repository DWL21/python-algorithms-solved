N = int(input())
current_number = 666
count = 0
answers = []
while True:
    if len(answers) == 10000:
        break
    if str(current_number).find("666") != -1:
        answers.append(current_number)
    current_number += 1
answer = answers[N-1]
print(answer)
