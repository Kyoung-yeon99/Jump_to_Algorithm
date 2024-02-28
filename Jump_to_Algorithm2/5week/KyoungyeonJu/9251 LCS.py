# 1차원 배열로 푸는 법
A = list(input())  #  ACAYKP
B = list(input())  #  CAPCAK
na = len(A)
nb = len(B)
dp = [0]*nb

for i in range(na):
    cnt = 0  # 누적값
    for j in range(nb):
        if cnt < dp[j]:  # 글자가 다른 경우, 누적값을 이전 위치까지의 최대값으로 갱신
            cnt = dp[j]
        elif A[i] == B[j]:  # 글자가 같은 경우, 누적값+1 넣어주기
            dp[j] = cnt+1
    # print(dp)

print(max(dp))



"""
# 2차원 배열로 푸는 방법
S1 = list(input())
S2 = list(input())
len1 = len(S1)
len2 = len(S2)
dp = [[0]*(len2 + 1) for _ in range(len1+1)]
print(dp)

for i in range(len1):
    for j in range(len2):
        if S1[i] == S2[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])

for i in range(len1+1):
    print(dp[i])

print(dp[len1][len2])

"""