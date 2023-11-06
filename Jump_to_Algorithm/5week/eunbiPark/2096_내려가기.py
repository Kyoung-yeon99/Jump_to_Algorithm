# 내려가면서 min, max 선택하기
# nums[i][0] -> nums[i+1][0], nums[i+1][1] 선택 가능
# nums[i][1] -> nums[i+1][0], nums[i+1][1], nums[i+1][1] 선택 가능
# nums[i][2] -> nums[i+1][1], nums[i+1][2] 선택 가능

'''
maxDP1[i] = arr[i][0] + max(maxDP1[i-1], maxDP2[i-1])
maxDP2[i] = arr[i][1] + max(maxDP1[i-1], maxDP2[i-1], maxDP3[i-1])
maxDP3[i] = arr[i][2] + max(maxDP2[i-1], maxDP3[i-1])
'''

# 메모리 초과 -> 슬라이딩 윈도우
# 사용하지 않는 값을 저장하지 않고 새롭게 배열에 갱신

n = int(input())

# 첫 3 숫자 받아 초기화
nums = list(map(int, input().split()))
max_dp = nums
min_dp = nums

for _ in range(n-1):
    nums = list(map(int, input().split()))
    # 입력받을 때마다 dp 갱신
    max_dp = [nums[0] + max(max_dp[0], max_dp[1]), nums[1] + max(max_dp), nums[2] + max(max_dp[1], max_dp[2])]
    min_dp = [nums[0] + min(min_dp[0], min_dp[1]), nums[1] + min(min_dp), nums[2] + min(min_dp[1], min_dp[2])]

print(max(max_dp), min(min_dp))