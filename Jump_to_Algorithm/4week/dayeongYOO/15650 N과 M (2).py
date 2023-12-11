n, m = map(int, input().split())

nums = []  # 숫자가 담길 스택


def dfs(depth, i):
    if depth == m:  # 재귀함수로 반복 -> 함수 출력 조건을 먼저 걸어준다.
        print(' '.join(map(str, nums)))
        return

    for j in range(i + 1, n + 1):
        if not visited[j]:  # 사용하지 않은 수라면
            visited[j] = True  # 사용한 수 체크
            nums.append(j)  # 수열에 추가
            dfs(depth + 1, j)  # 다음 +1 번째 수열을 위해 재귀함수 호출
            visited[j] = False  # 이전 상태로 돌아가기
            nums.pop()


visited = [False] * (n + 1)  # 이미 방문한 경우라면 제외하자.
dfs(0, 0)
