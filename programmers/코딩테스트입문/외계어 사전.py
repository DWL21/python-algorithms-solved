def is_valid(word, spell):
    for i in word:
        if i not in spell:
            return False
    if len(spell) == len(word) and len(set(list(word))) == len(word):
        return True
    return False


def solution(spell, dic):
    for i in dic:
        if is_valid(i, spell):
            print(i)
            return 1
    return 2


print(solution(["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"]))