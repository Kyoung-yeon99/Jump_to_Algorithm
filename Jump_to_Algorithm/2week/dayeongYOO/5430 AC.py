# https://www.acmicpc.net/problem/5430
from collections import deque

tc = int(input())  # 테스트 케이수 개수
for t in range(tc):
    command = input()  # 명령어
    n = int(input())  # 배열에 들어있는 수의 개수
    q = deque(input()[1:-1].split(','))  # 입력 배열의 파싱  # ','를 기준으로 자른다.

    flag = 0 # R 개수 세기

    if n == 0:  # 배열에 숫자가 없다면
        q = [] # 빈 큐 생성
    for c in command: # 명령어를 하나씩 탐색
        if c == 'R': # 배열 뒤집기
            flag += 1
        elif c == 'D':
            if len(q) == 0: # 큐에 아무것도 없다면
                print('error') # 에러 발생
                break
            else:
                if flag % 2 == 1: # R이 홀수라면
                    q.pop() # 제일 끝 요소를 추출
                else: # R이 짝수라면
                    q.popleft() # 제일 앞 요소를 추출
    else:
        if flag % 2 == 1: # 만약 마지막에 R이 홀수일 경우
            q.reverse() # 큐를 반전
        print('[' + ','.join(q) + ']')
