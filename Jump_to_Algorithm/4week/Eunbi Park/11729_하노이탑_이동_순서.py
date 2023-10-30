n = int(input())

def top(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        top(n-1, a, c, b)
        print(a, c)
        top(n-1, b, a, c)

ret = 2 ** n - 1
print(ret)

top(n, 1, 2, 3)