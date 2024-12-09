# 1은 켜져 있음, 0은 꺼져 있음
# 남학생이 받은 수가 배수이면, 그 스위치의 상태 바꾼다
# 여학생이 받은 수를 중심으로 좌우 대칭 구간을 찾아, 그 구간에 속한 스위치 상태 바꾼다

n = int(input())  # 1 <= n <= 100
switch = list(map(int, input().split()))
students = int(input())  # 1 <= n <= 100
for _ in range(students):
    gender, num = map(int, input().split())
    if gender == 1:
        idx = num
        while idx <= n:
            switch[idx-1] = (switch[idx-1]+1) % 2
            idx += num
    else:
        switch[num-1] = (switch[num-1]+1) % 2
        for i in range(1, n//2+1):
            if 1 <= num-i and num+i <= n and switch[num-i-1] == switch[num+i-1]:
                switch[num-i-1] = (switch[num-i-1] + 1) % 2
                switch[num+i-1] = (switch[num+i-1] + 1) % 2
            else:
                break

for i in range(len(switch)):
    if i > 0 and i % 20 == 0:  # 한 줄에 20개씩 출력
        print()
    print(switch[i], end=" ")


