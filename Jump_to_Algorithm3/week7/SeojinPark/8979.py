nation, key = map(int, input().split())
nation_medal=[]
for i in range(nation):
    lst = list(map(int, input().split()))
    nation_medal.append(lst)

# 금메달, 은메달, 동메달 수로 정렬하기
nation_medal.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

# key의 나라의 인덱스를 추출
idx = [nation_medal[i][0] for i in range(nation)].index(key)

for i in range(nation):
    # 같은 값이면 가장 앞에 있는 등수가 출력
    if nation_medal[idx][1:] == nation_medal[i][1:]:
        print(i+1) #1등부터~
        break
