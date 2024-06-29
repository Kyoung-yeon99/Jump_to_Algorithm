from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    reporter_set = defaultdict(set) # 신고자 : {신고당한자1, 신고당한자2, ...}
    warning = defaultdict(int)  # 경고 받은 횟수

    for a in report:
        reporter, reported = a.split()
        if reported not in reporter_set[reporter]:
            reporter_set[reporter].add(reported)
            warning[reported] += 1

    for a in id_list:
        cnt = 0
        for user in reporter_set[a]:
            if(warning[user] >= k):
                cnt += 1
        answer.append(cnt)

    return answer