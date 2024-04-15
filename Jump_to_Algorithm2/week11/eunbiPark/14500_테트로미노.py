n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 블럭의 초기 위치 저장 (회전 모양도 모두) - dxs, dys = [], []
blocks = {
    # -
    0: [[0, 0, 0, 0], [0, 1, 2, 3]],
    1: [[0, 1, 2, 3], [0, 0, 0, 0]],
    # ㅁ
    2: [[0, 0, 1, 1], [0, 1, 0, 1]],
    # ㄴ
    3: [[0, 1, 2, 2], [0, 0, 0, 1]],
    4: [[0, 1, 2, 2], [1, 1, 0, 1]],
    5: [[0, 0, 1, 2], [0, 1, 0, 0]],
    6: [[0, 0, 1, 2], [0, 1, 1, 1]],
    7: [[0, 0, 0, 1], [0, 1, 2, 0]],
    8: [[0, 0, 0, 1], [0, 1, 2, 2]],
    9: [[0, 1, 1, 1], [2, 0, 1, 2]],
    10: [[0, 1, 1, 1], [0, 0, 1, 2]],
    # ㄹ
    11: [[0, 1, 1, 2], [0, 0, 1, 1]],
    12: [[0, 0, 1, 1], [1, 2, 0, 1]],
    13: [[0, 1, 1, 2], [1, 0, 1, 0]],
    14: [[0, 0, 1, 1], [0, 1, 1, 2]],
    # ㅏ
    15: [[0, 1, 1, 2], [0, 0, 1, 0]],
    16: [[0, 0, 0, 1], [0, 1, 2, 1]],
    17: [[0, 1, 1, 2], [1, 0, 1, 1]],
    18: [[0, 1, 1, 1], [1, 0, 1, 2]]
}

# 블럭 초기 모양 확인
'''
for i in range(19):
    temp = [[0] * 5 for _ in range(5)]
    for dx, dy in zip(blocks[i][0], blocks[i][1]):
        temp[dx][dy] = 1

    print(i)
    for b in temp:
        print(*b)
    print()
'''

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    return True

# main
ans = 0
for x in range(n):
    for y in range(m):
        # 시작 위치
        for k in range(19): # 모든 블럭 확인
            temp = 0 # 임시로 board 값 더할 곳 (중간에 범위 넘어가면 버림)
            cnt = 0 # 4개 다 범위 안 인지 확인
            for dx, dy in zip(blocks[k][0], blocks[k][1]):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny):
                    cnt += 1
                    temp += board[nx][ny]

            if cnt == 4:
                ans = max(ans, temp)

print(ans)