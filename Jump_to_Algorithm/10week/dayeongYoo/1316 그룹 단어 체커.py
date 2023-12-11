# n: 단어 개수
from collections import defaultdict

n = int(input())
# 정답 초기화
ans = 0


def check_word(words):
    # 단어저장 dict
    dic = defaultdict(int)  # key 값을 int(0)으로 설정
    # 연속 글자인지 체크할 변수
    prev = words[0]
    # key로 문자 저장
    for w in words:
        if w not in dic:
            dic[w] += 1  # 없는 키 에러 해결-> 디폴트 딕셔너리
            prev = w  # 이전 문자 갱신

        else:
            if w != prev:  # 앞 글자와 다른 글자일때
                return False
    return True


# n개의 줄에 걸쳐 단어 입력
for _ in range(n):
    words = input()

    if check_word(words):  # 그룹단어라면
        ans += 1
print(ans)
