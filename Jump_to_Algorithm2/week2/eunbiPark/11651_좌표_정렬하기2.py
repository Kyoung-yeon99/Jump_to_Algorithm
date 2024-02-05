n = int(input())
dot = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

dot.sort(key = lambda x:(x[1], x[0])) # 정렬 순서, 방식

for d in dot:
    print(*d)