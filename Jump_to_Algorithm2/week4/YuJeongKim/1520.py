
m,n=map(int,input().split())

graph=[]

for _ in range(m):
    graph.append(list(map(int,input().split())))

dp = [ [-1]*n for _ in range(m)]


dx=[-1,1,0,0]
dy=[0,0,1,-1]

def dfs(x,y):

    if x==m-1 and y==n-1:
        return 1

    if dp[x][y]!=-1:
        return dp[x][y]

    if dp[x][y] == -1:

        dp[x][y]=0

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<m and 0<=ny<n and graph[x][y]>graph[nx][ny]:
                dp[x][y] += dfs(nx,ny)

    return dp[x][y]



print(dfs(0,0))