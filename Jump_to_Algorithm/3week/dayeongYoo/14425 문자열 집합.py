n, m = map(int, input().split())

s = set()
# n개의 문자열 집합
for _ in range(n):
    s.add(input())
# M개의 문자열 중에 총 몇 개가 집합 S에 포함되어 있는지
cnt = 0
string_lst = []
for _ in range(m):
    t = input()
    if t in s:
        cnt += 1

print(cnt)
