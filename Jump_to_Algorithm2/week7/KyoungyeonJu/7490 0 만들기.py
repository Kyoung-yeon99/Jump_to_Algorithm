from itertools import product  # 중복순열
tc = int(input())
for _ in range(tc):
    n = int(input())
    seq = [i for i in range(1, n+1)]
    # 출력은 ASCII 순서 따라서 " "(공백) 32, "+" 43, "-" 45
    aa = list(product([" ", "+", "-"], repeat=n-1))  # 3**(n-1)
    for a in range(len(aa)):
        string = '1'  # 항상 시작은 1이기 때문에
        for i in range(n-1):
            string = string+aa[a][i]+str(seq[i+1])  # 식 만들기
        expression = string.replace(" ", "")  # 공백 없애기
        result = eval(expression)  # 문자열 식을 받아서 계산

        if result == 0:
            print(string)

    print()  # 각 테스트 케이스의 결과를 한 줄 띄워 구분
