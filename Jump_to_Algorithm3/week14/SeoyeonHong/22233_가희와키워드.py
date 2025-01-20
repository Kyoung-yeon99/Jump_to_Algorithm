import sys
from collections import defaultdict

input = sys.stdin.readline
N, M = map(int, input().split()) # 키워드 개수, 글의 개수

keyword_list = defaultdict(int) # 기본값 0
for _ in range(N):
    keyword_list[input().rstrip()] = 1

count = N # 메모장에 남아 있는 키워드의 개수
for _ in range(M):
    for kw in list(input().rstrip().split(',')):
        if keyword_list[kw] > 0: # 메모장에 키워드가 있으면
            keyword_list[kw] -= 1
            count -= 1
    print(count) 
    