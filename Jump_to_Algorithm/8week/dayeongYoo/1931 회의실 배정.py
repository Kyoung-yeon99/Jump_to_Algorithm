n = int(input())
arr = []
ans = 0  # 정답

for _ in range(n):
    s, e = map(int, input().split())
    arr.append((s, e))

arr.sort(key=lambda x: (x[1], x[0]))  # 끝나는 시간으로 배열 정렬

e = 0 # 처음 시작 값 초기화
# 시작하자마자 끝나는 회의 고려
for ns, ne in arr:  # next start, next end
    if ns >= e:  # 다음 회의 시작 시간이 현재 끝나는 시간보다 크다면
        ans += 1
        e = ne  # 현재 끝나는 시간에 다음 끝나는 시간을 대입
print(ans)
