# 각 국가의 금, 은, 동메달 정보를 입력받아서, 어느 국가가 몇 등을 했는지 알려주는 프로그램
N, K = map(int, input().split()) # 국가의 수, 등수를 알고 싶은 국가
info = []
for _ in range(N):
    info.append(list(map(int, input().split()))) # 국가, 금, 은, 동메달의 수

info = sorted(info, key=lambda x: [-x[1], -x[2], -x[3]])
info[0].append(1)

rank = 1
draw = 1

for i in range(1, N):
    if info[i-1][1:4] == info[i][1:4]: # 이전 국가와 메달 개수가 같을 경우
        draw += 1
        info[i].append(rank)
    else: # 이전 국가보다 등수가 낮다면
        rank += draw
        info[i].append(rank)
        draw = 1
    
    if info[i][0] == K: # 등수를 알고 싶은 국가일 경우
        print(info[i][4])
        break


    