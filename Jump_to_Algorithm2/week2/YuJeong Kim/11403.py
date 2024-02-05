n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

def dfs(start):
    for i in range(n):
        if arr[start][i] == 1 and check[i]==0:
            check[i] = 1
            dfs(i)

check = [0 for _ in range(n)]
for i in range(n):
    dfs(i)
    print(*check)
    check = [0 for _ in range(n)]