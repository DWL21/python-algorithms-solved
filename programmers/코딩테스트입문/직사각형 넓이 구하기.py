def solution(dots):
    x_dots = list(map(lambda x: x[0], dots))
    y_dots =  list(map(lambda x: x[1], dots))
    return (max(x_dots) - min(x_dots)) * (max(y_dots) - min(y_dots))
