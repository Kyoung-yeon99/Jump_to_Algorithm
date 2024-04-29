from collections import deque

n = int(input()) # 전체 사람의 수
a, b = map(int, input().split()) # 촌수를 계산해야 하는 두 사람의 번호
m = int(input()) # 관계의 개수
r = [[] for _ in range(n+1)] # 1촌 리스트
v = [False for _ in range(n+1)] # 방문 여부
relative = False

for _ in range(m):
    x, y = map(int, input().split())
    r[y].append(x)
    r[x].append(y)

q = deque([(a, 0)])
v[a] = True

while q: # bfs
    p, c = q.popleft()
    if p == b:
        relative = True
        break
    for np in r[p]:
        if not v[np]:
            q.append((np, c+1))
            v[np] = True

print(c) if relative else print(-1)
    
    
    
