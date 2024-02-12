n, m = map(int, input().split())

ret = []

def dfs():
    # 다 뽑았으면
    if len(ret) == m:
        print(' '.join(map(str, ret)))
        return

    for i in range(1, n + 1): # 하나씩 뽑음
        if i not in ret: # 뽑히지 않았다면
            ret.append(i) # 배열에 추가
            dfs() # 문자열 개수 확인 + 다음 수 뽑기
            ret.pop() # 다 뽑아서 다음 조합을 만들어야 함 -> 하나 빼고 다시 만들기

dfs()