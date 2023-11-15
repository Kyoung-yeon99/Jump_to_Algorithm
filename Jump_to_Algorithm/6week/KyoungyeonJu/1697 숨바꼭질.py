from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())  # 0 <= n, k <= 100,000
max = 100000
cnt = [0] * (max+1)  # 해당 숫자(인덱스)까지 몇번 연산했는지 저장하는 리스트, visited이자 연산횟수 계산
qu = deque([n])

while True:
    n = qu.popleft()
    if n == k:  # 동생을 만나면
        print(cnt[n])  # 연산 횟수 print
        break

    # 동생을 아직 못 만났다면
    for i in (n-1, n+1, n*2):  # 이동연산
        #print("n=",n, "i=",i)
        # 조건문 cnt[i] == 0 먼저 작성하면 IndexError
        if 0 <= i <= max and cnt[i] == 0:  # 숫자 범위에 들어오고 연산된 적 없으면, 연산이 이미 된 건 계산X
            cnt[i] = cnt[n] + 1  # 연산 전 숫자의 연산 횟수 + 1
            qu.append(i)  # 스택 삽입
            #print(qu, cnt[i])

