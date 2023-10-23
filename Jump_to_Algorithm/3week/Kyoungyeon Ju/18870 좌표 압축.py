# 시간 초과....
import sys
input_ = sys.stdin.readline

n = int(input_())  # 1 ≤ N ≤ 1,000,000
a = list(map(int, input_().split()))  # 입력값 리스트 -10^9 ≤ Xi ≤ 10^9
sorted_a = sorted(a)
hashmap = dict()
idx = 0

for i in sorted_a:  # 정렬된 리스트에서 값 꺼내기
    if i not in hashmap:  # 해쉬멥에 존재하는 않는 값이면
        hashmap[i] = idx
        idx += 1

result = []
for i in a:  # 정렬되지 않은 처음 리스트에서 값 꺼내기
    result.append(hashmap[i])  # 해쉬맵에서 값을 가져오기

print(*result)


"""
# 리스트의 인덱스 찾는 부분에서 시간 초과
a = list(map(int, input_().split()))  # 입력값 리스트 -10^9 ≤ Xi ≤ 10^9
sorted_a = sorted(a)
result = []

for i in a:
    count = sorted_a.index(i)  # 정렬된 리스트의 인덱스 값, 중복 값들은 가장 첫 번째 인덱스 반환
    result.append(count)

print(*result)
"""

"""
# list, set&list&sorted, dict
n = int(input())
a = list(map(int, input().split()))
sa = sorted(list(set(a)))
da = dict()
for i in range(len(sa)):
    da[sa[i]] = i

for k in a:
    print(da[k], end=' ')
"""

