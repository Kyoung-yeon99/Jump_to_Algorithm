exp = input() # 쇠막대기와 레이저의 배치를 나타내는 괄호 표현
s = [] # 괄호 짝을 확인하기 위한 스택
count = 0 # 잘려진 쇠막대기 조각의 총 개수
for i in range(len(exp)):
    if exp[i] == '(': # 닫는 괄호일 경우 push
        s.append('(')
    else:
        s.pop() # 여는 괄호일 경우 pop
        if exp[i-1] == '(': # 레이저일 경우
            count += len(s) # 닫는 괄호 개수만큼 조각 수 추가
        else: # 막대의 끝일 경우
            count += 1 # 잘려진 조각 추가
print(count)
    
    