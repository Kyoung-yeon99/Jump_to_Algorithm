# n: 정수 개수, 합: s
n, s = map(int, input().split())
num = list(map(int, input().split()))

cnt = 0 # 부분 수열 개수 저장
ans = []# 부분 수열 저장


# 백트래킹
def back(start):
    global cnt

    if sum(ans) == s and len(ans) > 0:  # s일때 개수 증가, 크기가 양수인 부분수열
        cnt += 1

    for i in range(start, n):  # 깊이: start 부터 다음 탐색 진행
        ans.append(num[i]) # 현재 원소를 부분 수열에 추가
        back(i + 1)        # 재귀: 다음 원소 포함한 부분 수열 탐색(현재 이후 원소만 고려)
        ans.pop()          # 백트래킹 수행!: 부분수열에서 현재 원소 제거


# 함수 실행
back(0)
print(cnt)  # 부분 수열 개수 출력
