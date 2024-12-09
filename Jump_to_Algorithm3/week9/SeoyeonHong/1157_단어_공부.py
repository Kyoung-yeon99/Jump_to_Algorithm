# 알파벳 대소문자로 된 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램
from collections import Counter

word = str.upper(input()) # 모두 대문자로 변환
counter = Counter(word).most_common()
if len(counter) == 1 or counter[0][1] != counter[1][1]: # 가장 많이 사용된 알파벳이 한 개인 경우
    print(counter[0][0])
else: # 가장 많이 사용된 알파벳이 여러 개 존재하는 경우
    print('?')