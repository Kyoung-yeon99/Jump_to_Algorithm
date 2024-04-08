# 저렴한 주유소가 나오면 주유
n = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))

ans = 0
dist = 0
cheap = oil[0]
for i in range(1, n):
    dist += road[i - 1]
    if oil[i] < cheap: # 저렴한 주유소 등장
        ans += (dist * cheap) # 여기서 새로 주유할 것 -> 이전 값 계산
        cheap = oil[i] # 주유소 정보 변경
        dist = 0 # 이동 거리 0

ans += (dist * cheap) # 마지막 값 계산
print(ans)