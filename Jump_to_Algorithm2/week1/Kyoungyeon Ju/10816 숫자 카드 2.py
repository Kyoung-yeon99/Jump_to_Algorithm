import sys
input = sys.stdin.readline
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

# n_list를 dict으로
n_dict = dict()
for i in n_list:
    if n_dict.get(i) is None:  # 딕셔너리에 아직 key가 없는 경우
        n_dict[i] = 1
    else:  # 이미 key가 있는 경우
        n_dict[i] += 1

# 탐색과 출력
for i in m_list:
    if i in n_dict.keys():
        print(n_dict[i], end=' ')
    else:
        print(0, end=' ')


"""
# 1. 딕셔너리 자료형에서 in 사용
n_dict = dict()
for i in n_list:
    if i in n_dict: # 이미 key가 있는 경우
        n_dict[i] += 1
    else:  
        n_dict[i] = 1

# 2. collections.Counter 사용
import collections

N = int(input())
num_list = collections.Counter(map(int,input().split()))

M = int(input())
find = list(map(int,input().split()))

for num in find :
    print(num_list[num], end=" ") 
"""