a, b = map(int, input().split())
gcd, lcm = 1, 1
for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        gcd = i
        lcm = gcd * (a // i) * (b // i)
        break
print(gcd)
print(lcm)
