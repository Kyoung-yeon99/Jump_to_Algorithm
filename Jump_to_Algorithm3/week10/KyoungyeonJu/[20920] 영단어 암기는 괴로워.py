# 길이가 M 이상인 단어들을 외우기 위해 아래 우선순위를 적용하여 단어장 만들기
# 1. 자주 나오는 단어일수록 앞에 배치
# 2. 단어의 길이가 길수록 앞에 배치
# 3. 알파벳 순서대로 앞에 배치
import sys
from collections import Counter

input = sys.stdin.readline
n, m = map(int, input().split())  # 1 <= n <= 100000, 1 <= m <= 10
words = []

for _ in range(n):
    word = input().rstrip()
    if len(word) >= m:
        words.append(word)

dictionary = sorted(Counter(words).items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for key, values in dictionary:
    print(key)
