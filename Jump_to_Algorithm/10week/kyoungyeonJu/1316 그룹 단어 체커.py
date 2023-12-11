# 모든 문자들이 연속해서 나타나는 단어가 그룹 단어
n = int(input())
cnt = 0

for _ in range(n):
    word = input()
    chars = []
    GroupWord = True
    for i in range(len(word)):
        if word[i] not in chars:  # 새로운 문자
            chars.append(word[i])
        elif word[i] == word[i-1]:  # 바로 전과 같은 문자
            continue
        else:  # 새로운 문자도 아니고 직전 문자와 같지 않으면 그룹문자가 아니다
            GroupWord = False
            break
    if GroupWord:
        cnt += 1

print(cnt)

