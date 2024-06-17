# https://school.programmers.co.kr/learn/courses/30/lessons/160586

def solution(keymap, targets):
    answer = []
    dp = {} # 문자: 문자를 작성하기 위해 키를 눌러야 하는 최소 횟수
    for key in keymap:
        for i in range(len(key)):
            if key[i] in dp:
                dp[key[i]] = min(dp[key[i]], i) # 최소 횟수(인덱스 값) 저장
            else:
                dp[key[i]] = i
                    
    for target in targets:
        count = 0 # 키를 눌러야 하는 최소 횟수
        for key in target:
            if key in dp:
                count += dp[key] + 1 # 최소 횟수(인덱스 값 + 1) 더하기
            else: # 문자열을 작성할 수 없는 경우
                count = -1
                break
        answer.append(count)
    return answer