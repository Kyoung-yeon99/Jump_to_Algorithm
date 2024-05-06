import sys
input = sys.stdin.readline

n, c = map(int, input().split())
houses = [int(input()) for _ in range(n)]
houses.sort()

def install(mid):
    cnt = 1 # 하나 설치하고 시작해서 0이 아닌 1
    before = houses[0] # 이전 설치 위치
    for i in range(1, n):
        if houses[i] >= before + mid:
            cnt += 1
            before = houses[i]

    if cnt >= c:
        return True
    else:
        return False

start = 1
end = houses[-1] - houses[0]

# 공유기 사이 거리를 기준으로 이분 탐색
# 항상 일정한 거리를 유지해야 하는지
while start <= end:
    mid = (start + end) // 2

    if install(mid): # 더 넓게 설치 가능
        start = mid + 1
    else:
        end = mid - 1

print(end)