vowels=set('aeiou')
accept=['oo','ee']

while(True):
    flag=True
    password=input()
    if password=='end':
        break
    # 모음 측정
    if not (set(password) & vowels):
        print(f'<{password}> is not acceptable.')
        continue
    for i in range(len(password)-2):
        # 세개가 전부 모음
        if password[i] in vowels and password[i + 1] in vowels and password[i + 2] in vowels:
            flag=False
            break
        elif password[i] not in vowels and password[i + 1] not in vowels and password[i + 2] not in vowels:
            flag=False
            break
    if flag==False:
        print(f'<{password}> is not acceptable.')
        continue
    # 두개 연속 겹치는 알파벳
    for i in range(len(password) - 1):
        if password[i]==password[i+1]:
            if password[i] != 'e' and password[i] != 'o':
                flag=False
                break
    if flag==False:
        print(f'<{password}> is not acceptable.')
        continue
    print(f'<{password}> is acceptable.')