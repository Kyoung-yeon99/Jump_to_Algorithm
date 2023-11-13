from collections import deque


def bfs(start):
    qu = deque()
    qu.append(start)
    while qu:
        a = qu.popleft()
        if a == k:
            print(visited[a])
            return
        for i in (a - 1, a + 1, 2 * a):
            # print("n=",n, "i=",i)
            if 0 <= i <= max_num and visited[i] == 0:
                qu.append(i)
                visited[i] = visited[a] + 1
                parent[i] = a
                # print(qu, visited[i], "i=", i, parent[i])


n, k = map(int, input().split())
max_num = 100000
visited = [0] * (max_num + 1)
parent = [0] * (max_num + 1)  # parent[자식] = 부모, 자식은 여러 값이지만 부모는 하나
bfs(n)

result = []
new_k = k
for _ in range(visited[k]+1):  #  5 17 경우 최소시간 visited[17]=4에 1 더하기
    result.append(new_k)
    new_k = parent[new_k]
    #print(new_k, result)

print(' '.join(map(str, result[::-1])))  # 메모리 41512KB 시간 164ms
#print(*result[::-1])                     # 메모리 48688KB 시간 148ms