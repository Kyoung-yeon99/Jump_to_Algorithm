t = int(input()) # 테스트 케이스 개수

for _ in range(t):
    vps = True
    s = [] # 괄호 짝을 확인하기 위한 스택
    ps = input()
    if '(' not in ps or ')' not in ps: # '(' 또는 ')'가 없는 경우
        vps = False
    else:
        for b in ps:
            if b == '(':
                s.append(b) # 닫는 괄호일 경우 push
            else:
                if len(s) == 0 : # 짝이 맞지 않을 경우
                    vps = False
                    break
                else:
                    s.pop() # 닫는 괄호일 경우 pop

    print('YES' if vps and len(s) == 0 else 'NO')

        
