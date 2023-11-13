from collections import deque

t = int(input())


def bfs():
    q = deque()
    q.append((home_x, home_y))

    while q:
        x, y = q.popleft()

        if abs(x - festival_x) + abs(y - festival_y) <= 1000:
            print('happy')
            return

        for i in range(n):  # 편의점 확인
            if not visited[i]:  # 방문하지 않았다면
                nx, ny = graph[i]  # 편의점의 좌표를 새로 뽑고
                if abs(x - nx) + abs(y - ny) <= 1000:  # 다음까지 갈 수 있다면
                    visited[i] = 1  # 방문체크
                    q.append((nx, ny))  # 큐 삽입
    print('sad')  # 도달하지 못할 경우
    return


for _ in range(t):
    n = int(input())
    home_x, home_y = map(int, input().split())
    graph = []

    for _ in range(n):
        x, y = map(int, input().split())
        graph.append((x, y))

    festival_x, festival_y = map(int, input().split())

    visited = [0 for _ in range(n + 1)]

    bfs()
