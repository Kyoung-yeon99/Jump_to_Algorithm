# 최단거리
import sys
from collections import deque

input = sys.stdin.readline
n = int(input()) # 전체 사람의 수
a, b = map(int, input().split()) # 촌수를 계산해야 하는 두 사람의 번호
m = int(input()) # 부모 자식들 간의 관계의 개수
relation = [[] for _ in range(n+1)] # 관계 리스트
for _ in range(m):
    x, y = map(int, input().split()) # 부모, 자식
    relation[x].append(y)
    relation[y].append(x)

checked = [False for _ in range(n+1)] # 확인 여부

def check_relation(p, c): # 번호, 촌수
    checked[p] = True # 확인했음으로 체크
    c += 1
    for np in relation[p]:
        if np == b: # b와 몇촌인지 찾았을 경우 출력 후 종료
            print(c)
            exit()
        elif not checked[np]: # 연결된 사람 탐색
            check_relation(np, c)

check_relation(a, 0)
print(-1)