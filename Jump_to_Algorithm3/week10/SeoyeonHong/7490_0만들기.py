from itertools import product
T = int(input())
operator = [' ', '+', '-']

for _ in range(T):
    N = int(input())
    seq = [str(i) for i in range(1, N+1)]

    for operators in product(operator, repeat=N-1): # 중복순열 이용
        formula = seq[0]
        for i in range(N-1):
            if operators[i] != ' ':
                formula += operators[i]
            formula += seq[i+1]
        result = eval(formula)

        if result == 0: # 수식 계산 결과가 0이면 출력
            formula = seq[0]
            for i in range(N-1):
                formula += operators[i] + seq[i+1]
            print(formula)
            
    print()
