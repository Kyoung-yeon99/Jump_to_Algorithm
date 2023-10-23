n = int(input())

# 그룹 단어 개수
cnt = 0

for _ in range(n):
    s = input()
    str_s = set()  # 나온 단어 저장할 집합
    str_s.add(s[0])

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:  # 전의 문자와 같다면 pass
            continue
        elif s[i] not in str_s:  # 전 문자와 다르고, 처음 나온 문자라면
            str_s.add(s[i])  # 집합에 추가
        else:  # 전 문자와 다르지만, 나왔던 문자라면
            break  # 탈출
    else:  # 그룹단어임
        cnt += 1

print(cnt)
