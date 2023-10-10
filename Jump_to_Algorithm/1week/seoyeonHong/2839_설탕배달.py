n = int(input())
a = 0 # 5kg 봉지의 개수
t = n 

if n // 5 >= 1: # n이 5 이상일 경우
    a = n // 5 
    t = n - a * 5
    if t == 0: # n이 5의 배수일 경우
        print(a)
    elif t % 3 == 0: # 5 * a + 3 = n인 경우
        print(a + (t // 3))
    else:
        while(a > 0): # a값을 줄여가며 5 * a + 3 * b = n인 a, b를 탐색
            a -= 1
            t = n - a * 5
            if t % 3 == 0:
                print(a + (t // 3))
                break
        if a == 0 and ((t % 3) != 0): # n이 3의 배수가 아닐 경우
            print(-1)
elif n == 3: # n < 5일 경우 n이 3일 때만 나누어떨어짐
    print(1)
else: 
    print(-1) # 나누어떨어지지 않을 경우

'''
5 * a + 3 * b = n 일 때 (a + b)의 값이 최소가 되려면 a가 가능한 최대값이 되어야 한다.
'''
