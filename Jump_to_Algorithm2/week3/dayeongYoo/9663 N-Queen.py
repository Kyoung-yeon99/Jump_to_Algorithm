# https://www.acmicpc.net/problem/9663

'''
# 백트래킹 기본 코드
check_node(node v):
    node u
    if(promising(v))
        if(v에 해답이 있다면):
            해답을 출력
        else:
            for(v의 모든 자식 노드 u에 대해):
                check_node(u)
'''
def n_queens(i, col):
    global ans
    n = len(col) - 1

    if promising(i, col):
        if i == n:  # 끝까지 도달했을 때
            # print(col[1:n + 1])
            ans += 1
        else:
            for j in range(1, n + 1):
                col[i + 1] = j
                n_queens(i + 1, col)
    return ans


def promising(i, col):  # 유망함수 구현
    k = 1
    flag = True
    while k < i and flag:
        # 대각선 체크
        if col[i] == col[k] or abs(col[i] - col[k]) == (i - k):
            flag = False
        k += 1
    return flag


n = int(input())
col = [0] * (n + 1)
ans = 0
print(n_queens(0, col))

