import sys
input = sys.stdin.readline


def func(idx):
    global cnt, result
    # result 리스트에 값이 있고(크기가 양수인 부분집합) 합이 s이면, cnt 증가
    if result and sum(result) == s:
        cnt += 1
    for i in range(idx, n):  # idx부터 n-1까지 인덱스 for문
        if i not in result_idx:  # result에 추가하는 조건이 값이면... 같은 값인 경우
            result.append(nums[i])
            func(i+1)
            result.pop()  # 지난 주 푼 N과 M(2) 문제


n, s = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
result, result_idx = [], []  # 값과 idx를 저장하는 리스트 두 개 사용
func(0)
print(cnt)

