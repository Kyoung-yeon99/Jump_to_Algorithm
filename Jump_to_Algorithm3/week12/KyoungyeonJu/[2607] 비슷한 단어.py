# 첫 번째 단어와 비슷한 단어 개수 찾기
# 1. 같은 구성 갖기 -> 같은 종류 문자, 같은 문자는 같은 개수
# 2. 한 단어에서 한 문자를 더하거나, 빼거나, 하나의 문자를 다른 문자로 바꾸어서 나머지 한 단어와 같은 구성 갖기
from collections import Counter


def transfer(w):  # 한 문자 바꾸기
    for c in set(first_c.keys()).intersection(word_c.keys()):
        m = min(first_c[c], word_c[c])
        first_c[c] -= m
        word_c[c] -= m
        if first_c[c] < 0 or word_c[c] < 0:
            return False
        if first_c[c] == 0:
            del first_c[c]
        if word_c[c] == 0:
            del word_c[c]

    if len(first_c) == 1 and len(word_c) == 1 and list(first_c.values()) == [1] and list(word_c.values()) == [1]:
        return True

    return False


def add(w):  # word 에 한 문자 더하기
    for c in word_c.keys():
        if c in first_c.keys():
            first_c[c] -= word_c[c]
            if first_c[c] < 0:
                return False
        else:
            return False
    return True


def subtract(w):  # word 에서 한 문자 빼기
    for c in first_c.keys():
        if c in word_c.keys():
            word_c[c] -= first_c[c]
            if word_c[c] < 0:
                return False
        else:
            return False
    return True


n = int(input())
words = [input() for _ in range(n)]
first = words[0]
answer = 0

for i in range(1, n):
    first_c = Counter(words[0])
    word = words[i]
    word_c = Counter(word)

    if first_c == word_c:
        answer += 1
    elif len(first) == len(word):
        if transfer(word):
            answer += 1
    elif len(first) == len(word)-1:
        if subtract(word):
            answer += 1
    elif len(first) == len(word)+1:
        if add(word):
            answer += 1

print(answer)
