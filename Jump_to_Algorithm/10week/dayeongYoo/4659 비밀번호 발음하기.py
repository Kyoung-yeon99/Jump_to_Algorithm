aeiou = ('a', 'e', 'i', 'o', 'u')  # 모음

while True:  # end가 나오기 전까지 반복
    words = input()
    if words == 'end':
        break
    # 모음 개수
    cnt = 0
    # 자음, 모음 구별 & 1번째 조건 판단 위해 모음 개수 세기
    for a in aeiou:
        if a in words:
            cnt += 1  # 모음 개수 +1
    # 1. 모음이 하나도 없다면
    if cnt < 1:
        print(f'<{words}> is not acceptable.')  # 출력
        # 다음 단어 탐색
        continue

    # 2. 모음, 자음이 연속 3개라면
    # 조건 카운트
    s = 0
    for i in range(len(words) - 2):
        if words[i] in aeiou and words[i + 1] in aeiou and words[i + 2] in aeiou:
            s = 1  # 연속 모음
        elif not (words[i] in aeiou) and not (words[i + 1] in aeiou) and not (words[i + 2] in aeiou):
            s = 1  # 연속 자음
    if s == 1:
        print(f'<{words}> is not acceptable.')  # 출력
        continue

    # 3. 같은 글자가 연속 2개인지, ee, oo만 허용
    # 조건 카운트
    t = 0
    for i in range(len(words) - 1):
        if words[i] == words[i + 1]:
            if words[i] == 'e' or words[i] == 'o':  # ee, oo 라면
                continue
            else:  # 그 외 연속 2개 단어라면
                t = 1
    if t == 1:
        print(f'<{words}> is not acceptable.')  # 출력
        continue
    # 3개 조건 패스 시 적합한 비밀번호
    print(f'<{words}> is acceptable.')  # 출력
