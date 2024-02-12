# N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 방법의 수
# 같은 행, 열 또는 대각선에 존재하면 안됨 == 행과 열의 합 또는 차가 같으면 안됨

N = int(input())
cnt = 0 # N개의 퀸을 배치하는 방법의 수
        
def placeQueen(pos, sum, diff): # pos[i]는 i번째 행에 위치하는 퀸의 열을 의미
    global cnt
    r = len(pos)
    if r == N: # N개의 퀸을 배치했을 경우
        cnt += 1 # 퀸을 놓는 방법 +1
    else:
        for c in range(N): # 현재 행의 각 열에 대하여
            if c not in pos and not sum[r+c] and not diff[r-c+N]: # 같은 열 또는 대각선에 퀸이 없을 경우
                pos.append(c) # 현재 위치에 퀸을 배치
                sum[r+c] = True
                diff[r-c+N] = True
                placeQueen(pos, sum, diff) # 다음 퀸을 배치할 방법 탐색
                pos.pop() # 현재 위치에 퀸을 배치하는 방법을 모두 탐색했을 경우 다른 위치에 퀸을 배치했을 때의 경우 탐색
                sum[r+c] = False
                diff[r-c+N] = False

placeQueen([], [False for _ in range(N+N)], [False for _ in range(N+N)])
print(cnt)




# 시간 초과
# N = int(input())
# cnt = 0 # N개의 퀸을 배치하는 방법의 수

# def diagonal(pos, c): # 대각선에 다른 퀸이 위치할 경우 True, 없을 경우 False 반환
#     r = len(pos)
#     sum, diff = r+c, r-c
#     for i in range(r):
#         if i+pos[i] == sum or i-pos[i] == diff: # 행과 열의 합 또는 차가 같을 경우 같은 대각선에 위치
#             return True
#     return False
        
# def placeQueen(pos): # pos[i]는 i번째 행에 위치하는 퀸의 열을 의미
#     global cnt
#     if len(pos) == N: # N개의 퀸을 배치했을 경우
#         cnt += 1 # 퀸을 놓는 방법 +1
#     else:
#         for i in range(N): # 현재 행의 각 열에 대하여
#             if i not in pos and not diagonal(pos, i): # 같은 열 또는 대각선에 퀸이 없을 경우
#                 pos.append(i) # 현재 위치에 퀸을 배치
#                 placeQueen(pos) # 다음 퀸을 배치할 방법 탐색
#                 pos.pop() # 현재 위치에 퀸을 배치하는 방법을 모두 탐색했을 경우 다른 위치에 퀸을 배치했을 때의 경우 탐색

# placeQueen([])
# print(cnt)