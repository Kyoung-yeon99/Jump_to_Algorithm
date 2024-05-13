n, r, c = map(int, input().split())

# 정답
ans = 0

# 분할정복
while n != 0:
    # 재귀 탈출 조건
    n -= 1
    # 2사분면
    if r < 2 ** n and c < 2 ** n:
        ans += (2 ** n) * (2 ** n) * 0
    # 1사분면
    elif r < 2 ** n and c >= 2 ** n:
        ans += (2 ** n) * (2 ** n) * 1
        c -= (2 ** n)
    # 3사분면
    elif r >= 2 ** n and c < 2 ** n:
        ans += (2 ** n) * (2 ** n) * 2
        r -= (2 ** n)
    # 4사분면
    else:
        ans += (2 ** n) * (2 ** n) * 3
        r -= (2 ** n)
        c -= (2 ** n)
print(ans)

# # dfs
#
# # 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래
# dx = [0, 0, 1, 1]
# dy = [0, 1, -1, 1]
#
# n, r, c = map(int, input().split())
#
# # 맵 만들기
# board = [[0 for i in range(2 ** n)] for j in range(2 ** n)]
# print(board)
#
# # 맵 크기
# n = 2 ** n - 1
#
# # z 방향대로 숫자 채우기
# def dfs(x, y):
#     for i in range(4):
#         nx = x+dx[i]
#         ny = y+dy[i]
#         if 0<=nx<n and 0<=ny<n and board[nx][ny]==0: # 아직 방문 안했다면
#             board[nx][ny] += 1
#             dfs(nx, ny)
# dfs(0,0)
# print(board)
#
# # 배열에 숫자 채운후 좌표에 해당하는 값 찾으려고 했으나 n이 15까지 가능하니까 ... 2의 15승 * 2의 15승 -> 이렇게 하는거 아님^^
