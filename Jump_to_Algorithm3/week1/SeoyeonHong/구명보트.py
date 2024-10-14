# https://school.programmers.co.kr/learn/courses/30/lessons/42885

# 필요한 구명보트(2인승) 개수의 최솟값
def solution(people, limit):
    boat = 0 # 구명보트 개수
    n = len(people) # 총인원
    people.sort() # 오름차순 정렬
    s = 0 
    e = n-1 
    while s <= e:
        if people[e] + people[s] > limit: # 무거운 사람 혼자 태우기
            e -= 1
            boat += 1
        else: # 가장 가벼운 사람과 가장 무거운 사람을 같이 태우기
            e -= 1
            s += 1
            boat += 1

    return boat