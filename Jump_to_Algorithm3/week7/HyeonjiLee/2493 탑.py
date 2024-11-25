from sys import stdin
N = int(stdin.readline().rstrip())
arr = list(map(int, stdin.readline().rstrip().split()))
answer = [0] * N 
stack = [] 

for i in range(N):
    # 현재 탑의 높이가 스택의 탑보다 클 때 스택에서 제거
    while stack and stack[-1][0] < arr[i]:
        stack.pop()

    # 스택이 비어있지 않으면, 스택의 마지막 탑이 신호를 수신
    if stack:
        answer[i] = stack[-1][1] + 1  # 인덱스는 1부터 시작하므로 +1

    # 현재 탑 스택에 추가
    stack.append((arr[i], i))

print(*answer)
