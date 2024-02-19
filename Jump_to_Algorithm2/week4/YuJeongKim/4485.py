# 상하좌우 이동
# 잃는 금액 최소로 . 최단경로

import heapq
INF=int(1e9)

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def dijkstra():

    q=[]
    heapq.heappush(q, (arr[0][0], 0, 0))

    while q:
        c, x, y = heapq.heappop(q)

        if x==n-1 and y==n-1:
            print("Problem %d: %d" % (count, distance[x][y]))
            break

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<n:
                _cost=c+arr[nx][ny]

                if _cost < distance[nx][ny]:
                    distance[nx][ny]=_cost
                    heapq.heappush(q, (_cost, nx, ny))



count=1
while True:
    n=int(input())

    if n==0:
        break

    arr=[]
    for _ in range(n):
        arr.append(list(map(int,input().split())))


    distance = [ [INF]*n for _ in range(n) ]

    dijkstra()
    count+=1