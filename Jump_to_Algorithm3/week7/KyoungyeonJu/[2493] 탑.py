import sys

input = sys.stdin.readline
n = int(input())
tops = list(map(int, input().split()))
answer = []

stack = []  # 탑의 인덱스
for i in range(n):
    while stack and tops[stack[-1]] < tops[i]:
        stack.pop()
    if stack:
        answer.append(stack[-1]+1)
    else:
        answer.append(0)
    stack.append(i)

print(" ".join(map(str, answer)))


"""
# 시간 초과 - 최악의 경우 O(n^2)
now = n - 1
while now > -1:
    idx = now - 1
    while idx > -1 and tops[idx] < tops[now]:
        idx -= 1
    answer.append(idx+1)
    now -= 1

print(' '.join(map(str, answer[::-1])))
"""
