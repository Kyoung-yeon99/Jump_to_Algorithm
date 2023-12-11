from collections import defaultdict

# 사진 틀 개수
n = int(input())
# m: 총 추천 횟수
m = int(input())
# 추천받은 순서
reco = list(map(int, input().split()))
# 추천 횟수 저장
temp = defaultdict(int)

for i in range(m):
    # 추천
    temp[reco[i]] += 1
    if len(temp) > n:  # 꽉 찼을경우
        # 최소 요소 삭제 준비
        least = float('inf')
        # 추천 받은 사람을 돌면서
        for j in temp:
            if j == reco[i]:  # 중복 추천
                continue
            if temp[j] < least:  # 현재까지 추천받은 횟수가 가장 적은 학생 삭제
                target = j
                least = temp[j]
        del temp[target]

# 오름차순으로 출력
ans = []
for t in temp:
    ans.append(t)
ans.sort()
print(*ans)
