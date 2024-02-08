# 아홉개의 수 중 합이 100이 되는 일곱 개의 수
num = [] # 아홉개의 수
for _ in range(9):
    num.append(int(input()))
total = sum(num) # 아홉개의 수의 합
    
for i in range(8): # 제외해야 하는 숮자 찾기
    for j in range(i+1, 9):
        if total - num[i] - num[j] == 100: # 합이 100인 일곱개의 수를 찾았을 경우
            for a in range(9):
                if a != i and a != j: # 일곱개의 숫자 출력
                    print(num[a])
            break # 반복문 종료