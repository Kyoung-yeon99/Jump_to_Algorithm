# 연산 수행 프로그램
import sys

input = sys.stdin.readline
M = int(input())
S = [False for _ in range(21)] # 공집합

for _ in range(M):
    cmd = input().split()
    if len(cmd) == 2:
        cmd[1] = int(cmd[1])
    if cmd[0] == 'add': # S에 x를 추가
        S[cmd[1]] = True
    elif cmd[0] == 'remove': # S에서 x를 제거
        S[cmd[1]] = False
    elif cmd[0] == 'check': # S에 x가 있으면 1을, 없으면 0을 출력
        print(1 if S[cmd[1]] else 0)
    elif cmd[0] == 'toggle': # S에 x가 있으면 x를 제거하고, 없으면 x를 추가
        S[cmd[1]] = not S[cmd[1]]
    elif cmd[0] == 'all': # S를 {1, 2, ..., 20} 으로 변경
        S = [True for _ in range(21)] 
    else: # S를 공집합으로 변경
        S = [False for _ in range(21)] 