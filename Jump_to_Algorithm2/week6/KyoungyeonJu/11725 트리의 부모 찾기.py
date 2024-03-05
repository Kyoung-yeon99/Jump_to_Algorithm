from collections import deque
import sys
input = sys.stdin.readline

n = int(input())  # 2 ≤ N ≤ 100,000 존많
m = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    m[a].append(b)
    m[b].append(a)

ans = [False]*(n+1)

# bfs
q = deque()
q.append(1)  # 루트 1
while q:
    node = q.popleft()
    for nn in m[node]:  # 루트의 자식들
        if not ans[nn]:  # 부모 노드를 저장하지 않는 노드
            ans[nn] = node  # 부모 노드 저장
            q.append(nn)

for i in ans[2:]:  # 2번 노드부터 부모 노드 출력
    print(i)



# 처음에 defaultdict 쓰다가 틀림
