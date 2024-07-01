# https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    suspended = [] # 이용 정지된 사용자 목록
    rn = {id: 0 for id in id_list} # 신고된 횟수
    rl = {id: [] for id in id_list} # 신고한 사람 목록
    mail = {id: 0 for id in id_list} # 받은 이메일 개수
    
    for i in range(len(report)):
        reporter, target = report[i].split()
        if target not in rl[reporter]: # 처음 신고했을 경우
            rl[reporter].append(target)
            rn[target] += 1
        
    for user in rn:
        if rn[user] >= k: # k번 이상 신고당했을 경우
            suspended.append(user)
    
    for id in id_list:
        for su in suspended:
            if su in rl[id]: # 신고한 사람이 이용 정지되었을 경우
                mail[id] += 1
    
    return list(mail.values())