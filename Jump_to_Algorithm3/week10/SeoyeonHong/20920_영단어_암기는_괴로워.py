import sys
from collections import defaultdict

input = sys.stdin.readline
N, M = map(int, input().split())
words = defaultdict(int)

for _ in range(N):
    word = input().rstrip()
    if len(word) >= M: # 길이가 M 이상인 단어일 경우
        words[word] += 1

words = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word in words:
    print(word[0])