n,m=map(int,input().split())

x,y,d=map(int,input().split())

arr=[ list(map(int,input().split())) for _ in range(n) ]

cnt=0

# 북 , 동 , 남 , 서
dx=[-1,0,1,0]
dy=[0,1,0,-1]


while True:

    if arr[x][y]==0:
        cnt+=1
        arr[x][y]=2

    find = False

    for i in range(4):
        # 왼쪽 방향
        d = (d + 3) % 4

        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
            x, y = nx, ny
            find = True
            cnt += 1
            arr[nx][ny]=2
            break

    if not find:
        # 현재 방향 , 후진
        nx, ny = x - dx[d], y - dy[d]

        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 1:
            x, y = nx, ny
        else:
            break


print(cnt)


