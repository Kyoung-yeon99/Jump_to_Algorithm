# 두 개의 서로 다른 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액을 찾기
N = int(input()) # 전체 용액의 수
s = list(map(int, input().split())) # 용액의 특성값
l, r = 0, N-1
mv = 2000000000 # 0에 가장 가까운 혼합 용액 특성값의 절댓값
answer = []

if s[r] < 0: # 모두 알칼리성(최댓값이 음수)일 경우
    answer = [s[r-1], s[r]]
elif s[l] > 0: # 모두 산성(최솟값이 양수)일 경우
    answer = [s[l], s[l+1]]
else: # 산성 용액과 알칼리성 용액이 모두 존재할 경우
    for i in range(N-1):
        v = s[l] + s[r] # 혼합 용액의 특성값
        if mv > abs(v): # 중성에 가까운 혼합 용액의 특성값 갱신
            mv = abs(v)
            answer = [s[l], s[r]]
        if v > 0: # 특성값이 양수일 경우
            r -= 1
        elif v < 0: # 특성값이 음수일 경우
            l += 1
        else: # 특성값이 0일 경우
            break # 탐색 중지
        
print(*answer)