# 1. y좌표가 증가하는 순
# 2. x좌표가 증가하는 순
# 점의 최대 개수와 좌표의 범위가 크므로 단순 정렬 시 시간초과 가능성 있음
    
c = {} # 점의 좌표값, 딕셔너리 자료구조
n = int(input()) # 점의 개수

for _ in range(n):
    x, y = map(int, input().split())
    if y not in c:
        c[y] = [x]
    else:
        c[y].append(x)

for y in sorted(c):
    for x in sorted(c[y]):
        print(x, y)


# 시간초과
# c = []
# n = int(input())
# for _ in range(n):
#     c.append(list(map(int, input().split())))

# c.sort(key = lambda x :(x[1], x[0]))
# for v in c:
#     print(*v)