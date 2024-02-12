n, m = map(int, input().split())

ret = []
def dfs(start):
    if len(ret) == m:
        print(*ret)
        return

    for i in range(start, n + 1): # 뽑지 않은 수 부터
        if i not in ret: # 해당 수가 뽑히지 않았다면
            ret.append(i) # 배열에 추가
            dfs(i + 1) # 뽑았으니 시작점 += 1
            ret.pop() # 다음 수 뽑을 수 있도록 자리 만들기

dfs(1)