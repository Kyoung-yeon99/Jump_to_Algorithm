T=int(input())

def dfs(n,idx,rst):
    if idx == n:
        # eval 함수를 활용하여 문자열 상태에서 연산이 가능하도록
        ans = eval(rst.replace(' ', ''))
        if ans == 0:
            res.append(rst)
        return
    else:
        n_idx = idx+1
        # 공백인 경우 숫자 이어붙이기
        dfs(n, n_idx,rst+' '+str(n_idx))
        # 덧셈의 경우
        dfs(n, n_idx, rst + '+' + str(n_idx))
        # 뺄셈의 경우
        dfs(n, n_idx, rst + '-' + str(n_idx))

for _ in range(T):
    n=int(input())
    res=[]
    dfs(n,1,'1')
    [print(a) for a in res]
    print()