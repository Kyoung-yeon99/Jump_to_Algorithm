def check(num):
    for i in range(num):
        # 같은 열인지, 같은 대각선 위에 위치하는지 확인
        if row[num] == row[i] or abs(row[num] - row[i]) == num - i:
            return False
    return True


def nqueen(num):
    global ans
    if num == n:  # 모든 조건에 맞게 퀸을 놓았으면
        ans += 1  # 퀸 놓는 방법의 수 증가
        return

    for i in range(n):  # 각 행에 퀸 놓기
        row[num] = i
        if check(num):  # 퀸을 놓을 수 있는지 행,열,대각선 확인
            nqueen(num+1)


n = int(input())
row = [0] * n
ans = 0
nqueen(0)
print(ans)  # Python3 시간초과, PyPy3 통과 ?!
