x, y = map(int, input().split(' '))


def gcd(a, b):
    if b > a:
        a, b = b, a
    while True:
        if b == 0:
            break
        a, b = b, a % b
    return a

print(x + y - gcd(x, y))