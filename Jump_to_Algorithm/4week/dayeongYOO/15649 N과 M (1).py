n, m = map(int, input().split())

nums = []  # 숫자가 담길 스택


def dfs():
    if len(nums) == m:  # 재귀함수로 반복 -> 함수 출력 조건을 먼저 걸어준다.
        print(' '.join(map(str, nums)))
        return

    for i in range(1, n + 1):  # 1부터 n까지의 자연수 중 선택
        if i in nums:  # 이미 선택한 숫자라면..
            continue  # 경우의 수에서 배제 -> 백트래킹

        nums.append(i)  # 스택에 추가
        dfs()  # 동작 후
        nums.pop()  # 스택에서 제거 -> 이전의 상황으로 돌아옴.


dfs()
