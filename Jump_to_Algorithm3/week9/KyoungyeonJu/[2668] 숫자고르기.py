# 첫째 줄에서 뽑은 숫자의 집합과
# 뽑힌 숫자들의 바로 밑에 들어있는 숫자들이 이루는 집합이 일치하도록
# 최대로 많이 뽑아서 첫째 줄에 뽑힌 정수 개수와 뽑힌 정수 오름차순으로 출력


def dfs(v):
    if not visited[v]:
        visited[v] = True
        first.add(v)
        second.add(graph[v][0])
        print("dfs first", first, "second", second)
        if first == second:
            answer.update(list(first))
            return
        dfs(graph[v][0])



n = int(input())
graph = [[] for _ in range(n+1)]
answer = set()
for i in range(1, n+1):
    graph[i].append(int(input()))

for i in range(1, n+1):
    visited = [False] * (n + 1)
    first, second = set(), set()
    dfs(i)
    print("return answer", answer, "first", first, "second", second)

answer = sorted(answer)
print(len(answer))
for ans in answer:
    print(ans)
