test_case = int(input())


def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    return f(n - 3) + f(n - 2) + f(n - 1)


for i in range(test_case):
    n = int(input())
    print(f(n))