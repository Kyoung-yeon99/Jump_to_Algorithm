def solution(players, callings):
    result = {p: i for i, p in enumerate(players)}

    for c in callings:
        # 인덱스 구하는 과정을 아래 코드로 변경
        # idx = players.index(c)
        idx = result[c]
        result[c] -= 1
        result[players[idx - 1]] += 1
        players[idx - 1], players[idx] = players[idx], players[idx - 1]

    return players

    '''
    # 시간 초과
    for c in callings:
        idx = players.index(c)
        players[idx], players[idx-1] = players[idx-1], players[idx]
    return players
    '''

    '''
    # 한번에 순위 적용 - 순서가 중요해서 안됨 
    hash = {}
    for c in callings:
        if c not in hash:
            hash[c] = 1
        else:
            hash[c] += 1

    for h in hash:
        idx = players.index(h)
        players[idx], players[idx-2] = players[idx-2], players[idx]
    return players
    '''

