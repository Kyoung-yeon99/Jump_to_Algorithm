import sys
input = sys.stdin.readline

n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]
# 끝나는 시간이 빠른 순으로 정렬
# 끝나는 시간이 같다면 시작하는 시간이 빠른 순으로 정렬 <- 시작하자 끝나는 회의 고려
time.sort(key=lambda x: (x[1], x[0]))

result = 0
t = 0
for s, e in time:
    if s < t:
        # print("t=",t,"s=",s)
        continue
    # 시작 시간이 현재 시간 보다 같거나 크면
    result += 1
    t = e
    print("result=", result, "t=", t)

print(result)


