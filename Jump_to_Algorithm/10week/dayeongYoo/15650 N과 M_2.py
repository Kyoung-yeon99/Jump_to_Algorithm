n, m = map(int, input().split())
arr = []


def dfs(start):
    # 길이가 m이 되었다면
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    # 1~n 중에서 1개 뽑기
    for i in range(start, n + 1):
        if i not in arr:  # ab, ba는 같은 코드임.
            arr.append(i)
            dfs(i + 1)
            arr.pop()


dfs(1)
