n, d = map(int, input().split())
shortcut = []
dp = [i for i in range(d+1)]

for _ in range(n):
    a, b, c = map(int, input().split())
    if b - a > c and b <= d:  # 지름길이면서 고속도로 길이 이하인 지름길만 저장
        shortcut.append([a, b, c])

for i in range(d+1):
    if i > 0:
        dp[i] = min(dp[i], dp[i-1]+1)  # 이전 값에 1을 더한 값과 비교하여 작은 수 선택
    for s, e, d in shortcut:
        if i == s and dp[i] + d < dp[e]:
            dp[e] = dp[i] + d

print(dp[-1])


"""
n, d = map(int, input().split())
shortcut = []
s = []
dp = [i for i in range(d+1)]
for _ in range(n):
    a, b, c = map(int, input().split())
    if b - a > c and b <= d:  # 지름길이면서 고속도로 길이 이하인 지름길만 저장
        shortcut.append([a, b, c])
        s.append(a)

for i in range(d+1):
    if i > 0:
        dp[i] = min(dp[i], dp[i-1]+1)  # 이전 값에 1을 더한 값과 비교하여 작은 수 선택
    for s, e, d in shortcut:
        if i == s and dp[i] + d < dp[e]:
            dp[e] = dp[i] + d
            print(e, dp[e])

print(dp[-1])
"""





