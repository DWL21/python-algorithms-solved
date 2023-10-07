SUCCESS_MESSAGE = 'login'
NOT_FOUND = 'fail'
UNAUTHORIZED = 'wrong pw'


def solution(id_pw, db):
    data = dict()
    for x, y in db:
        data[x] = y
    id, pw = id_pw
    if id in data and data[id] == pw:
        return SUCCESS_MESSAGE
    elif id in data:
        return UNAUTHORIZED
    return NOT_FOUND
