# 1부터 N까지의 오름차순 수열에 '+', '-', ''을 삽입한 결과가 0이 되는 수식 출력
T = int(input())
N = 0

def make_expression(idx, exp):
    global N
    if idx <= N:
        make_expression(idx+1, exp+" "+str(idx)) # ' ' 연산자와 숫자 추가
        make_expression(idx+1, exp+"+"+str(idx)) # '+' 연산자와 숫자 추가
        make_expression(idx+1, exp+"-"+str(idx)) # '-' 연산자와 숫자 추가
        
    else:
        if (eval(exp.replace(" ", ""))) == 0: # 공백 제거, 연산 결과가 0일 경우 출력
            print(exp)

for _ in range(T):
    N = int(input())
    make_expression(2, "1")
    print()