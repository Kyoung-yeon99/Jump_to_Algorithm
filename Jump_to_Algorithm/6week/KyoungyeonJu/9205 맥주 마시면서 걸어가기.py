from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque()
    q.append(start)
    while q:
        x, y = q.popleft()
        if abs(end[0]-x) + abs(end[1]-y) <= 1000:
            #print(end[0], x, abs(end[0]-x), end[1], y, abs(end[1]-y))
            print("happy")
            return
        for i in range(con_n):
            if visited[i] == 0 and abs(con[i][0]-x)+abs(con[i][1]-y) <= 1000:
                q.append([con[i][0], con[i][1]])
                visited[i] = 1
                #print("i=",i,con[i][0],x,abs(con[i][0]-x),con[i][1],y,abs(con[i][1]-y))
    print("sad")
    return


t = int(input())  # 테스트케이스 수
for _ in range(t):
    con_n = int(input())  # 편의점 수
    con = []
    start = list(map(int, input().split()))  # 상근이네 위치
    for _ in range(con_n):  # 편의점 위치
        con.append(list(map(int, input().split())))
    end = list(map(int, input().split()))  # 페스티벌 위치

    visited = [0] * con_n  # 출발 도착 제외, 편의점
    bfs()

