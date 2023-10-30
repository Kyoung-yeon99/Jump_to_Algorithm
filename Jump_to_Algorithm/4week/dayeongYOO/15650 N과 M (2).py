# 백트래킹=> dfs 가지치기

def dfs(depth, i):
    if depth == m:  # 재귀함수로 반복 -> 함수 출력 조건을 먼저 걸어준다.
        print(' '.join(map(str, nums)))
        return
    for j in range(i + 1, n + 1):
        if not visited[j]:
            visited[j] = True
            nums.append(j)
            dfs(depth + 1, j)  # 다음
            visited[j] = False
            nums.pop()


n, m = map(int, input().split())
nums = []  # 숫자가 담길 스택
visited = [False] * (n + 1)  # 이미 방문한 경우라면 제외하자.
dfs(0, 0)
