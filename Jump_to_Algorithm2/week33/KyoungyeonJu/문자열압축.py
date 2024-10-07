def solution(s):
    answer = len(s)  # 처음에 1000이라고 했다가, 테케5 len(s)=1인 경우 오류
    l = len(s)

    for i in range(1, l//2+1):
        ans = ''
        cnt = 1
        unit = s[:i]
        for j in range(i, l, i):
            if unit == s[j:j+i]:  # 반복되면
                cnt += 1
            else:  # 반복되지 않으면
                if cnt > 1:
                    ans += str(cnt) + unit
                else:
                    ans += unit
                unit = s[j:j+i]
                cnt = 1

        if cnt > 1:
            ans += str(cnt) + unit
        else:
            ans += unit

        answer = min(answer, len(ans))

    return answer