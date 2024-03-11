import sys
input = sys.stdin.readline

n = int(input())
list = [int(input()) for _ in range(n)]
list.sort()
INF = int(1e9)
mini = INF

for i in range(n):  # n-1라고 하면 틀림
    cnt = 0
    for j in range(i+1, n):
        if list[j] - list[i] <= 4:  # max와 min 차이가 4
            cnt += 1
    if cnt >= 4:
        cnt = 4
    mini = min(mini, 4-cnt)

print(mini)


"""
# 다른 풀이법
temp = []
for i in range(n):
    cnt = 0
    for j in range(list[i], list[i]+5):
        if j not in list:
            cnt += 1
    temp.append(cnt)
    
print(min(temp))
"""