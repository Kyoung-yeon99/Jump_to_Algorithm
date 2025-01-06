# 첫 번째 단어와 비슷한 단어가 모두 몇 개인지 찾아 출력
import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
first_word = input().rstrip()
l = len(first_word)
counter = defaultdict(int)
for w in first_word:
    counter[w] += 1
answer = 0

for _ in range(N-1):
    word = input().rstrip()
    if l-1 <= len(word) <= l+1:
        diff = counter.copy() # 문자 종류별 개수의 차이
        for w in word:
            diff[w] -= 1
        
        total_diff = 0
        for d in diff:
            total_diff += abs(diff[d])
        
        if total_diff <= 2: # 다른 문자의 개수가 2개 이하일 경우
            answer += 1

print(answer)