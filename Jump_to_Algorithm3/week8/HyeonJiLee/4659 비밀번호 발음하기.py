from sys import stdin
vowel_list = ['a','e','i','o','u']
while True:
    password = stdin.readline().rstrip()
    if password == 'end':
     break
    #모음 또는 자음 연속 3개
    error = False
    min_vowel = False
    vowel = consonant = 0
    before = ''
    for s in password:
        # 모음 또는 자음 연속 3개 X
        if s in vowel_list:
            min_vowel = True # 모음 반드시 하나 포함
            if consonant != 0:
                consonant = 0
            vowel+=1
        else:
            if vowel != 0:
                vowel = 0
            consonant+=1
        if consonant >= 3 or vowel >= 3:
            error = True
            break
        # 같은 글자 연속 두번 오면 X, ee, oo는 제외
        if not before:
            before = s
        else:
            if (s == before) and (s not in ('e','o')):
                error = True
                break
            else:
                before = s
    if error or not min_vowel:
        print(f"<{password}> is not acceptable.")
    else:
        print(f"<{password}> is acceptable.")