# https://school.programmers.co.kr/learn/courses/30/lessons/258712

def solution(friends, gifts): # friends: 친구들의 이름, gifts: 친구들이 주고받은 선물 기록
    gift_num = {} # 선물 지수
    people = len(friends)
    record = [[0 for _ in range(people)] for _ in range(people)]
    index = {friends[i]: i for i in range(people)}
    
    for friend in friends:
        gift_num[friend] = 0 
    for gift in gifts:
        a, b = gift.split() # a: 선물을 준 친구, b: 선물을 받은 친구
        gift_num[a] += 1
        gift_num[b] -= 1
        record[index[a]][index[b]] += 1

    expected = [0 for _ in range(people)]

    for a in range(people-1):
        for b in range(a+1, people):
            if record[a][b] > record[b][a]: # a가 b에게 더 많이 줬다면
                expected[a] += 1
            elif record[a][b] < record[b][a]: # b가 a에게 더 많이 줬다면
                expected[b] += 1
            else: # 선물을 주고받은 기록이 없거나 같다면
                if gift_num[friends[a]] > gift_num[friends[b]]: # a의 선물 지수가 더 크다면
                    expected[a] += 1
                elif gift_num[friends[a]] < gift_num[friends[b]]: # b의 선물 지수가 더 크다면
                    expected[b] += 1

    return max(expected) # 다음달에 가장 많은 선물을 받는 친구가 받을 선물의 수
