

def ccw(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    result = (x2 - x1)*(y3 - y1) - (x3 - x1)*(y2 - y1)
    if result > 0:
        return -1
    if result < 0:
        return 1
    return 0


L1 = list(map(int, input().split()))
L2 = list(map(int, input().split()))
a = tuple(L1[:2])
b = tuple(L1[2:])
c = tuple(L2[:2])
d = tuple(L2[2:])


def is_crossed(a, b, c, d):
    abc = ccw(a, b, c)
    abd = ccw(a, b, d)
    cda = ccw(c, d, a)
    cdb = ccw(c, d, b)
    ab = abc*abd
    cd = cda*cdb
    if not ab and not cd:
        if a > b:
            a, b = b, a
        if c > d:
            c, d = d, c
        return c <= b and a <= d
    return ab <= 0 and cd <= 0


if is_crossed(a, b, c, d):
    print(1)
else:
    print(0)
    
