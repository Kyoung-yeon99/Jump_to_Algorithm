N, score, P = map(int, input().split())
if N == 0: #랭킹 리스트 아무도 없으면 1등
    print(1)
else: #랭킹 리스트 있으면
    rank = list(map(int,input().split()))
    answer = -1

    #현재 랭킹 리스트 순회
    for i in range(N):
        if score > rank[i]: #현재 점수보다 높으면
            rank.insert(i, score) #해당 위치에 score 삽입
            answer = rank.index(score) + 1 #등수 설정
            break
    #새 점수가 삽입되지 않았고 랭킹리스트도 꽉안찬거면
    #맨 뒤에 score 삽입
    if len(rank) < P and answer == -1:
        rank.append(score)
        answer = rank.index(score) + 1

    print(answer)
