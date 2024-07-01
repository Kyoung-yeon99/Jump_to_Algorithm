# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    answer = ''
    q = len(survey)
    score = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0} # 유형별 점수
    
    for i in range(q):
        choice = choices[i]
        if choice < 4: # 앞의 유형 +
            score[survey[i][0]] += 4 - choice
        elif choice > 4: # 뒤의 유형 +
            score[survey[i][1]] += choice - 4
    
    answer += 'R' if score['R'] >= score['T'] else 'T'
    answer += 'C' if score['C'] >= score['F'] else 'F'
    answer += 'J' if score['J'] >= score['M'] else 'M'
    answer += 'A' if score['A'] >= score['N'] else 'N'
    
    return answer