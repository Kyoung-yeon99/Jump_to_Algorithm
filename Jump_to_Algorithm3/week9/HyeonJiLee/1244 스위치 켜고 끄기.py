N = int(input())+1 #스위치 인덱스 1부터 시작
switch = [-1] + list(map(int,input().split()))
students = int(input())
for _ in range(students):
    #남학생은 1
    gender, num = map(int, input().split())

    if gender == 1:
        for i in range(num,N,num):
            switch[i] = 0 if switch[i] == 1 else 1
    # 여학생은 2
    if gender == 2:
        # 대칭 구간 찾기
        left = num - 1
        right = num + 1

        switch[num] = 0 if switch[num] == 1 else 1
        while left > 0 and right < N:
            if switch[left] != switch[right]:
                break
            else:
                switch[left] = 0 if switch[left] == 1 else 1
                switch[right] = 0 if switch[right] == 1 else 1
            left -= 1
            right += 1


for i in range(1,len(switch),1):
    print(switch[i], end='')

    if i%20 == 0:
        print()
    else:
        print(end=' ')

