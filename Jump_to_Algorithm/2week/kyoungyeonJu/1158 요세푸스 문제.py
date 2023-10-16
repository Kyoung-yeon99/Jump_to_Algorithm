from collections import deque

n, k = map(int, input().split())

circle = deque([i for i in range(1, n+1)])
a = list()

while len(circle) > 0:
    circle.rotate(-(k-1))
    a.append(circle.popleft())


a = list(map(str, a))
a = "<"+", ".join(a)+">"
print(a)
