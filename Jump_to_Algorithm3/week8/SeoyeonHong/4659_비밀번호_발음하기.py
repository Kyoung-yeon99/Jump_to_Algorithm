# 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
# 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
# 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.

import sys

input = sys.stdin.readline
vowel = 'aeiou'

while True:
    pw = input()[:-1]
    if pw == 'end':
        break
    acceptable = True
    
    if len(set(pw) & set (vowel)) == 0: # 모음이 하나도 없다면
        acceptable = False
    else:
        seq_len = 1
        for i in range(len(pw)-1):
            if (pw[i] in vowel) == (pw[i+1] in vowel): # 모음이나 자음이 연속될 경우
                if pw[i] == pw[i+1] and pw[i:i+2] != 'ee' and pw[i:i+2] != 'oo': # 'ee'와 'oo'를 제외하고 같은 글자가 연속적으로 두번 나올 경우
                    acceptable = False
                    break
                if seq_len == 1:
                    seq_len += 1
                else: # 모음 또는 자음이 3개 연속으로 올 경우
                    acceptable = False
                    break
            else: # 모음-자음 또는 자음-모음이 올 경우
                seq_len = 1

    if acceptable:
        print(f'<{pw}> is acceptable.')
    else:
        print(f'<{pw}> is not acceptable.')
