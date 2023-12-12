while 1:
    word = input()
    if word == 'end':
        break

    # x: 조건 2 flag
    # y: 조건 3 flag
    x = y = 0

    # 조건 1: 모음 개수 세기
    cnt = 0
    for i in 'aeiou':
        if i in word:
            cnt += 1

    if cnt < 1:
        print(f'<{word}> is not acceptable.')
        continue

    # 조건 2: 연속 3개 체크
    for i in range(len(word) -2):
        if word[i] in 'aeiou' and word[i + 1] in 'aeiou' and word[i+2] in 'aeiou':
            x = 1
        elif not (word[i] in 'aeiou') and not (word[i + 1] in 'aeiou') and not (word[i+2] in 'aeiou'):
            x = 1
    if x == 1:
        print(f'<{word}> is not acceptable.')
        continue

    # 조건 3: 같은 글자 2개 이상 ('aa', 'ee' 제외)
    for i in range(len(word) -1):
        if word[i] == word[i + 1]:
            if word[i] == 'e' or word[i] == 'o':
                continue
            else:
                y = 1

    if y == 1:
        print(f'<{word}> is not acceptable.')
        continue

    print(f'<{word}> is acceptable.')