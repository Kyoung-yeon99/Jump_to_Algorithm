# 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수
n = int(input()) #회의의 수
m = [] # 회의 시작 시간, 회의 끝나는 시간
for _ in range(n):
    m.append(list(map(int, input().split())))
m.sort(key = lambda x : (x[0], (x[1] - x[0]))) # 끝나는 시간과 소요 시간을 기준으로 정렬

time = 0
count = 0

for i in range(n):
    if time <= m[i][0]: # 이전 회의와 겹치지 않을 경우 회의실 배정
        count += 1
        time = m[i][1]
    elif time > m[i][1]: # 이전의 회의보다 더 일찍 끝날 경우 현재 회의로 변경
        time = m[i][1]

print(count)
