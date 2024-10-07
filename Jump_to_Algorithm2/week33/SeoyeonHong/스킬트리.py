# https://school.programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    answer = 0 # 가능한 스킬트리의 개수
    
    for st in skill_trees:
        index = []
        for s in st:
            i = skill.find(s) # 배워야 하는 스킬의 순서
            if i > -1: # 순서가 상관 있을 경우 인덱스 추가
                 index.append(i)
                    
        if index == [i for i in range(len(index))]: # 첫번째 스킬부터 순서대로 배울 경우만 가능
            answer += 1

    return answer