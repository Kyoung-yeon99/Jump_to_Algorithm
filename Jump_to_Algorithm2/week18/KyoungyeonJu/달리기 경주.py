def solution(players, callings):
    players = ["mumu", "soe", "poe", "kai", "mine"]
    idx = players.index("kai")
    players.remove("kai")
    players.insert(idx, "kai")
    print(players)
    answer = []
    return answer




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