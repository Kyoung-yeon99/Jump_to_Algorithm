from itertools import product
N = int(input())
for _ in range(N):
    tc = int(input())
    prod = product(['+','-',''], repeat = tc-1)
    answer = []
    for p in prod:
        p = list(p) + [''] #숫자 = tc개, 연산자 = tc-1개, zip 시 길이 맞추기 위해 연산자에 '' 하나 추가
        exp = []
        for num, operator in zip(range(1,tc+1), p): #숫자 + 연산자 식 만들기
            exp.append(str(num))
            exp.append(operator)

        result = eval(''.join(exp)) #연산 결과 result에 저장

        if result == 0: #결과가 0이면 식 출력
            #붙어있는 값 ""-> 공백 " "으로 바꾸기
            #맨 마지막에 임시로 넣은 ""은 제외
            for i in range(len(exp)-1):
                if exp[i] == "":
                    exp[i] = " "
            #answer 리스트 추가
            answer.append(''.join(exp))
    #ascii 순서에 따라 정렬
    answer.sort()
    for exp in answer:
        print(exp)
    #tc 한줄 띄우기
    print()