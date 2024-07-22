# 점수의 합이 최대가 되면서 서로 변을 공유 하지 않는 스티커 집합
T = int(input()) # 테스트 케이스 개수
for _ in range(T):
    n = int(input())
    score = []
    dp = [[0, 0, 0] for _ in range(n)] # 위, 아래를 선택하거나 아무것도 선택하지 않았을 때의 최대 점수
    max_score = 0
    score.append(list(map(int, input().split())))
    score.append(list(map(int, input().split())))

    dp[0][0] = score[0][0]
    dp[0][1] = score[1][0]

    for i in range(1, n): # i번째 열에 대해
        dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + score[0][i] # 위를 선택할 경우
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + score[1][i] # 아래를 선택할 경우
        dp[i][2] = max(dp[i-1]) # 모두 선택하지 않을 경우

    print(max(dp[n-1]))
    
        
    
    
