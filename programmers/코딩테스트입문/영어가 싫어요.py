words = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7, 
    "eight": 8, 
    "nine": 9
}

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for key, value in words.items():
            if numbers[i: i + len(key)] == key:
                answer.append(value)
    return int(''.join(map(str, answer)))
