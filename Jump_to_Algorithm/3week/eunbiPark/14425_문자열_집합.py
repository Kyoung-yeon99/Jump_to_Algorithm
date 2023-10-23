n, m = map(int, input().split()) # n개로 이루어진 문자열 s, m 개의 문자열
# m 개의 문자열 중 s에 포함되어 있는 것이 몇개인지

s = [
    input()
    for _ in range(n)
]

# 검사해야 할 단어
find = [
    input()
    for _ in range(m)
]

cnt = 0
for f in find:
    if f in s:
        cnt += 1

print(cnt)