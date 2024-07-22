# https://school.programmers.co.kr/learn/courses/30/lessons/176963

def solution(name, yearning, photo):
    people = len(name) # 그리워하는 사람의 수
    score = {name[i]: yearning[i] for i in range(people)} # 이름: 그리움 점수
    answer = [] # 사진들의 추억 점수
    for p in photo: # 각 사진에 대해
        s = 0 # 사진의 추억 점수
        for n in p: # 사진 속 인물들에 대해
            if n in name: # 그리워하는 사람이라면
                s += score[n] # 그리움 점수 더하기
        answer.append(s) # 사진의 추억 점수 저장
    return answer