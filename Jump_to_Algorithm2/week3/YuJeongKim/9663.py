# n*n 체스판, 퀸 n개 공격 x 경우의수 -> 완탐

# 1. 각 행에 퀸 하나
# 2. 왼쪽아래에서 오른쪽 위 대각선 방향 체크
# 3. 왼쪽위에서 오른쪽 아래 대각성 방향 체크


n=int(input())
arr=[0 for _ in range(n)]

sum=0

def check(r1, c1, r2, c2):
    if c1==c2:
        return False
    if r1-c1==r2-c2:    # 조건 2
        return False
    if r1+c1==r2+c2:    # 조건 3
        return False
    return True


def recur(row):
    if row==n:
        global sum
        sum+=1
    else:
        for c in range(n):
            possible=True
            # row 이전 행에 놓인 퀸 체크
            for r in range(row):
                if not check(row, c, r, arr[r]):
                    possible=False
                    break

            if possible:
                arr[row]=c
                recur(row+1)
                arr[row]=0

recur(0)

print(sum)