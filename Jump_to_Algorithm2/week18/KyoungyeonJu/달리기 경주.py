def solution(players, callings):
    # 선수는 키, 인덱스는 키인 딕셔너리
    d = {player: idx for idx, player in enumerate(players)}

    for c in callings:
        idx = d[c]  # 추월한 선수의 현재 위치
        d[c] -= 1  # 추월한 선수의 추월 후 위치
        d[players[idx-1]] += 1  # 추월 당한 선수의 추월 후 위치
        players[idx-1], players[idx] = players[idx], players[idx-1]  # 리스트에서 선수들의 위치 swqp

    return players

"""
5 ≤ players의 길이 ≤ 50,000
2 ≤ callings의 길이 ≤ 1,000,000

시간초과

    for i in range(len(callings)):
        player = callings[i]
        idx = players.index(player)
        players.remove(player)
        players.insert(idx-1, player)

"""