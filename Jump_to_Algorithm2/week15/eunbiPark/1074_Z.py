n, r, c = map(int, input().split())

def recursion(n, row, col):
    if n == 0: # 2^1 * 2^1 까지 확인했다면 return
        return 0

    # 현재 위치: (2 * 행 + 열)
    cur = 2 * (row % 2) + (col % 2)

    # 한 위치에서 행과 열을 2로 나눈 위치는 기존 값의 1/4
    return 4 * recursion(n-1, row//2, col//2) + cur

print(recursion(n, r, c))