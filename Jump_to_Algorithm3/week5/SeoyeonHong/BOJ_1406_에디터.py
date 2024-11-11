# 명령어가 차례로 주어졌을 때, 모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 구하는 프로그램
import sys
input = sys.stdin.readline
l = list(input())[:-1] # 초기 문자열
r = []
M = int(input()) # 명령어의 개수

for _ in range(M):
    c = input().split()
    if c[0] == 'L':
        if l: 
            r.append(l.pop())
    elif c[0] == 'D':
        if r:
            l.append(r.pop())
    elif c[0] == 'B':
        if l:
            l.pop()
    else:
        l.append(c[1])
print(''.join(l + r[::-1]))
    