while True:
    pw = input()
    if pw == 'end':
        break
    acceptable = True
    noVowel = True

    for p in pw: # 모음이 있는지 확인
        if p in 'aeiou':
            noVowel = False
            break

    if noVowel:
        print(f'<{pw}> is not acceptable.')
        continue

    v, c = 0, 0 # 연속되는 모음, 자음 개수
    for i in range(len(pw)): # 연속되는 문자 확인
        if pw[i] in 'aeiou': # 모음일 경우
            v += 1
            c = 0
            if v == 2:
                if pw[i] != 'e' and pw[i] != 'o':
                    if pw[i] == pw[i-1]:
                        acceptable = False
                        break
            elif v == 3:
                acceptable = False
                break
        else:
            c += 1
            v = 0
            if c == 2:
                if pw[i] == pw[i-1]:
                    acceptable = False
                    break
            elif c == 3:
                acceptable = False
                break

    if acceptable:
        print(f'<{pw}> is acceptable.')
    else:
        print(f'<{pw}> is not acceptable.')