# 모두 0 -> 0, 모두 1 -> 1
# 섞여 있다면 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래로 나누어 압축

# 1. 모든 값이 0 혹은 1로 이루어져 있는지 확인
    # (True) -> 해당 값 입력
    # (False) -> 사분면으로 분할 & 괄호
        # 1번으로 돌아가 다시 확인

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input()))) # str 값으로 받지 않도록 주의...

# 사분면으로 나눠가며 분할 정복

def dfs(x, y, n):
    # 검사 범위 내 가장 첫번째 값(왼쪽 위)을 기준점으로 잡기
    check = board[x][y]
    
    # 나눈 범위를 모두 돌며 다른 값으로 이루어져 있는지 확인 
    for i in range(x, x + n):
        for j in range(y, y + n):
            # 0과 1이 섞인 사분면이라면 
            if check != board[i][j]:
                check = -1
                break

    # 0과 1이 섞여 있다면 
    if check == -1:
        # 사분면 나누기 
        print('(', end='')
        # 범위 줄이기 
        n = n // 2
        # dfs로 분할 정복 (재귀)
        dfs(x, y, n)
        dfs(x, y + n, n)
        dfs(x + n, y, n)
        dfs(x + n, y + n, n)
        # 사분면 닫기 
        print(')', end='')

    # 모든 값이 1으로 이루어져 있다면 
    elif check == 1:
        print(1, end='')

    # 모든 값이 0으로 이루어져 있다면
    else:
        print(0, end='')

dfs(0, 0, n)