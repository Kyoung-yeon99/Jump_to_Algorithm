# 산성 용액 특성값은 양의 정수, 1부터 10**9
# 알칼리성 용액 특성값은 음의 정수, -1부터 -10**9
# 정렬된 특성값이 주어졌을 때, 이 중 두 개의 서로 다른 용액을 혼합하여
# 0에 가장 가까운 용액을 만들어내는 두 용액을 찾는 문제

# 이분탐색
n = int(input())  # 2 <= n <= 100,000
liq = list(map(int, input().split()))

start, end = 0, n-1
mini = abs(liq[start] + liq[end])  # 특성값의 범위를 봤을 때, int(1e9)는 부적절
a, b = liq[start], liq[end]

while start < end:  # start와 end가 같은 값인 경우 제외
    add = liq[start]+liq[end]
    if abs(add) < mini:
        mini = abs(add)
        a, b = liq[start], liq[end]

    if add < 0:  # 정렬된 특성값이 주어지므로 값의 음수와 양수 기준으로 탐색
        start += 1
    else:
        end -= 1

print(a, b)


"""
n = int(input())  # 2 <= n <= 10**5
liq = list(map(int, input().split()))
liq.sort(key=lambda x: abs(x))
mini, a, b = int(1e9), -1, -1

for i in range(n-1):
    add = abs(liq[i]+liq[i+1])
    if add < mini:
        mini = add
        a, b = min(liq[i], liq[i+1]), max(liq[i], liq[i+1])


print(a, b)
"""