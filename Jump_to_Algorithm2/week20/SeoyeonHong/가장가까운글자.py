# https://school.programmers.co.kr/learn/courses/30/lessons/142086

def solution(s):
    answer = []
    num = {} # 알파벳의 인덱스
    for i in range(len(s)):
        a = s[i]
        if a in num: # a가 이미 나왔을 경우
            answer.append(i - num[a]) # 몇 칸 앞에 같은 글자가 있는지 확인
            num[a] = i
        else: # a가 처음 나왔을 경우
            num[a] = i
            answer.append(-1)
    return answer