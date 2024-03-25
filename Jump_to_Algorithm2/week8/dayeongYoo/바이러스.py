# dfs

n = int(input())
m = int(input())

# graph = [list(map(int, input().split())) for _ in range(m)]
# 위와 같이 저장하면 안됨.

graph = [[] for _ in range(n + 1)]

# 각 노드에 연결관계를 저장해준다.
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 양방향

# 중복 방문 안됨
visited = [False] * (n + 1)
# 답
ans = 0


def dfs(x):
    global ans
    visited[x] = True  # 1번 컴퓨터 방문
    for i in graph[x]:
        if not visited[i]:  # 방문하지 않았다면
            dfs(i)
            ans += 1


dfs(1)  # 1번컴퓨터
print(ans)
