import sys
input = sys.stdin.readline

n = int(input())
RGB = [list(map(int, input().split())) for _ in range(n)]
dp = [RGB[0][0], RGB[0][1], RGB[0][2]]

# i번째 집을 R로 칠한다면, (i번째 R값+i-1번째 집이 G) (i번째 R값+i-1번째 집이 B) 두 값 중 더 작은 값 선택
for i in range(1, n):
    num0 = min(RGB[i][0] + dp[1], RGB[i][0] + dp[2])
    num1 = min(RGB[i][1] + dp[0], RGB[i][1] + dp[2])
    num2 = min(RGB[i][2] + dp[0], RGB[i][2] + dp[1])
    dp = [num0, num1, num2]

print(min(dp))
