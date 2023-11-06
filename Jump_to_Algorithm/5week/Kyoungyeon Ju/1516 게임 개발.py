import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
time = [0]
graph = [[] for _ in range(n+1)]  # 행 n+1, 2차 배열?
indegree = [0] * (n+1)  # 진입차수

for i in range(1, n+1):
    values = list(map(int, input().split()))[:-1] # 마지막 요소 -1 없애기
    t = values[0]  # 시간
    time.append(t)

    for value in values[1:]:
        graph[value].append(i)
        indegree[i] += 1

#print("graph",graph)
#print("indegree",indegree)
#print("time",time)


def topology_sort():
    result = [0] * (n+1)
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:  # 진입차수가 0인 노드를 queue로
            q.append(i)

    while q:
        now = q.popleft()
        result[now] += time[now]
        #print("now=",now, "result[now]=", result[now], "time[now]=",time[now])
        for g in graph[now]:
            indegree[g] -= 1
            result[g] = max(result[g], result[now])  # 동시에 건물 짓기가 가능하므로 먼저 지어야하는 건물들 중 최고로 많이 걸리는 시간을 더해주어야 한다.
            # 3번 건물을 짓기 위해 1번 건물 4초, 2번 건물 10초를 지어야 한다 -> 10초를 기다려야 3번 건물 짓기 가능
            print("g=",g,"result[g]=",result[g],"result[now]=",result[now])
            if indegree[g] == 0:
                q.append(g)

    return result


answers = topology_sort()
for i in range(1, n+1):
    print(answers[i])