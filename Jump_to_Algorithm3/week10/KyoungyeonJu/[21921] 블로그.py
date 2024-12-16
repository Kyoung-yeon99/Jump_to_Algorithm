# 블로그를 시작한 지 N일이 지나고 X일 동안 가장 많이 들어온 방문자 수와 기간 구하기
N, X = map(int, input().split())  # 1 <= X <= N <= 250,000
visitors = list(map(int, input().split()))
ans, ans_num = 0, 0
if sum(visitors) == 0:
    print("SAD")
else:
    window = sum(visitors[:X])
    ans, ans_num = window, 1
    for i in range(X, N):
        window = window - visitors[i-X] + visitors[i]
        if window > ans:
            ans = window
            ans_num = 1
        elif window == ans:
            ans_num += 1

    print(ans)
    print(ans_num)