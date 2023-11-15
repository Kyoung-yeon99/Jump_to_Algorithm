from collections import deque

n, k = map(int, input().split())
min_time = abs(n - k)
dp = [0 for _ in range(100001)]
visited = [False for _ in range(100001)]

def bfs(): # 너비 우선 탐색 - 큐
    global min_time
    q = deque()
    q.append(n)
    visited[n] = True
    while q:
        num = q.popleft()
        if num == k:
            min_time = dp[num]
            break
        for i in [num-1, num+1, num*2]:
            if 0 <= i < 100001:
                if not visited[i]:
                    q.append(i)
                    visited[i] = True
                    dp[i] = dp[num] + 1

if n < k: # 동생이 앞에 있을 경우 너비 우선 탐색, 동생이 뒤에 있을 경우 k - n만큼 시간 소요
    bfs()

print(min_time)