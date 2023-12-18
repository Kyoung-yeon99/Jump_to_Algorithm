# 가로와 세로 크기 M(2 ≤ M ≤ 700)과 날짜수 n
m, n = map(int, input().split())
# 격자
board = [1 for _ in range(2 * m - 1)]

for i in range(n):
    bees = list(map(int, input().split()))
    idx = 0
    for j in range(3): # 왼쪽, 왼쪽 위, 위쪽만 확인
        for k in range(bees[j]):
            board[idx] += j # 첫행, 첫열 애벌래들의 성장 수치를 더한다
            idx += 1
half = (2 * m - 1) // 2  # 중간지점 계산

new_board = board[half + 1:]
for i in range(half, -1, -1):  # 마지막 날 저녁의 크기를 첫행부터
    print(board[i], end=' ')
    for n in new_board:
        print(n, end=' ')
    print()
