import sys

input = sys.stdin.readline
S = int(input()) # 스위치의 개수
status = list(map(int, input().split())) # 각 스위치의 상태
N = int(input()) # 학생수

def switch(idx):
    status[idx] = 1 if status[idx] == 0 else 0

for _ in range(N):
    gender, number = map(int, input().split())
    idx = number - 1
    if gender == 1: # 남학생일 경우
        for i in range(idx, S, number): # 배수일 경우 스위치 상태 바꾸기
           switch(i)
    else: # 여학생일 경우
        switch(idx)
        for i in range(1, min(idx+1, S-idx)):
            if status[idx+i] == status[idx-i]: # 좌우 대칭이라면
                switch(idx+i)
                switch(idx-i)
            else:
                break

for i in range(S): # 20개씩 출력
    print(status[i], end = ' ')
    if (i+1) % 20 == 0:
        print()