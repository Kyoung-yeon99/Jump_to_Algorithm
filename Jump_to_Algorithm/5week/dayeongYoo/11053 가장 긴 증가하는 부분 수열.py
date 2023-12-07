n = int(input())  # 수열의 크기
arr = list(map(int, input().split()))  # 수열

cache = [-1] * n


def lis(i):
    # 이미 계산한 값일 경우
    if cache[i] != -1:
        return cache[i]

    ans = 1 # 가장 긴 증가하는 부분 수열의 초기값은 1임.
    for nxt in range(i + 1, n): # 수열의 크기만큼 다음 요소를 돌면서
        if arr[i] < arr[nxt]: # 만약 다음 요소가 더 크다면
            ans = max(ans, lis(nxt) + 1) # 최댓값 갱신
    cache[i] = ans # 캐시 테이블에 최댓값을 대입한다.
    return ans


max_length = 0  # Variable to store the maximum LIS length

for i in range(n):
    max_length = max(max_length, lis(i))

print(max_length)
