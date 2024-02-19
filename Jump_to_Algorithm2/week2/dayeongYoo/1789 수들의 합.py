# 서로 다른 n개의 자연수 합: s
# 자연수 n의 최댓값?

s = int(input())
# 합 변수
total = 0
cnt = 0

for i in range(1, s + 1):
    total += i
    cnt += 1
    if total > s:
        break


if s==1:
    print(1)
else:
    print(cnt - 1)  # total이 s보다 큰 경우이므로, -1 해준다
