import sys

n, m = map(int, input().split())
hashmap = dict()  # 해시맵
count = 0

for _ in range(n):
    str_ = sys.stdin.readline()
    hashmap[str_] = 1

for _ in range(m):
    str_ = sys.stdin.readline()
    if str_ in hashmap:
        count += 1

print(count)

