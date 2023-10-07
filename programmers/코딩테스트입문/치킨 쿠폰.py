def solution(chicken):
    service_chickens = 0
    coupon = chicken
    while coupon >= 10:
        service_chickens += coupon // 10
        coupon = coupon // 10 + coupon % 10
    return service_chickens
