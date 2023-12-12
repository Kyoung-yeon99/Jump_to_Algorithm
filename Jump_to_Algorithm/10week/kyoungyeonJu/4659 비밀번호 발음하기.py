# 모음 a e i o u  하나 반드시 포함
# 모듬 혹은 자음이 3개 연속 X
# 같은 문자가 연속 두번 오면 안되나, ee와 oo는 허용
vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    pw = input()
    if pw == 'end':
        break
    rule1 = False
    rule2 = True
    rule3 = True

    for char in pw:
        if char in vowel:
            rule1 = True
            break
    if rule1 is False:  # 모음이 없으면
        print(f'<{pw}> is not acceptable.')
        continue

    for i in range(len(pw)-2):
        three = pw[i:i+3]
        if three[0] in vowel and three[1] in vowel and three[2] in vowel: # 모음 연속 3개
            rule2 = False
        if three[0] not in vowel and three[1] not in vowel and three[2] not in vowel: # 자음 연속 3개
            rule2 = False
    if rule2 is False:  # 자음이나 모음이 연속 3개이면
        print(f'<{pw}> is not acceptable.')
        continue

    for i in range(len(pw)-1):
        if pw[i] == pw[i+1]:
            if pw[i] == 'e' or pw[i] == 'o':
                continue
            else:
                rule3 = False

    if rule3 is False:
        print(f'<{pw}> is not acceptable.')
        continue

    print(f'<{pw}> is acceptable.')





