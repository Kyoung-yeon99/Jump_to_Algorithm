# https://school.programmers.co.kr/learn/courses/30/lessons/178871

# 시간초과
def solution(players, callings):
    for calling in callings:
        index = players.index(calling)
        players[index], players[index-1] = players[index-1], players[index]

    return players


