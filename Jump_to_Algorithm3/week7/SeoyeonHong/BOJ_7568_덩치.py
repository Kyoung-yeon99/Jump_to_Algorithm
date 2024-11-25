# 키와 몸무게가 모두 클 경우 덩치가 더 크다고 한다
# 자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1이 된다
# -> 키와 몸무게의 합이 작으면 덩치가 더 클 수 없다

N = int(input()) # 사람의 수
people = [] # 키와 몸무게
rank = [0 for _ in range(N)] # 등수
for i in range(N):
    people.append([i] + list(map(int, input().split())))

people.sort(key= lambda x: -(x[1] + x[2])) # 키와 몸무게의 합을 기준으로 내림차순으로 정렬

for i in range(N):
    k = 0 # 덩치가 더 큰 사람의 수
    for j in range(i):
        if people[j][1] > people[i][1] and people[j][2] > people[i][2]: # 덩치가 더 클 경우
            k += 1
    rank[people[i][0]] = str(k + 1)

print(' '.join(rank))
