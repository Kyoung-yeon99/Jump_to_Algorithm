k = int(input())
a, b = 1, 0

for i in range(k):
    a, b = b, a+b

print(a, b)