# 새로운 점수가 랭킹 리스트에서 몇 등 하는지 구하는 프로그램

N, score, P = map(int, input().split())
ranking_list = list(map(int, input().split())) if N > 0 else []
rank = -1
appended = False
for i in range(N):
    if ranking_list[i] < score: # 랭킹 리스트에 있는 점수보다 새로운 점수가 크다면
        ranking_list.insert(i, score)
        rank = ranking_list.index(score) + 1
        appended = True
        break

if not appended and N < P: # 아직 랭킹 리스트에 올라가지 않았고 랭킹 리스트에 빈 자리가 있다면
    ranking_list.append(score)
    rank = ranking_list.index(score) + 1

print(rank)
