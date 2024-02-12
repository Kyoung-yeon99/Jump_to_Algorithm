n = int(input())

ret = 0
v1 = [0] * n
v2 = [0] * (2 * n)
v3 = [0] * (2 * n)

def dfs(row):
    global ret
    if row == n: # 탐색 완료 (끝까지 탈출 안하고 탐색)
        ret += 1 # 경우의 수 += 1
        return

    for j in range(n):
        if v1[j] == v2[row + j] == v3[row - j] == 0:
            v1[j] = v2[row + j] = v3[row - j] = 1
            dfs(row + 1)
            v1[j] = v2[row + j] = v3[row - j] = 0

dfs(0)
print(ret)
