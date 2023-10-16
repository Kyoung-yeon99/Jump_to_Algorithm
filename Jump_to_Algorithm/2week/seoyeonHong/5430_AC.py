from collections import deque

T = int(input()) # 테스트 케이스 개수

for _ in range(T):
    P = input() # 함수
    n = int(input()) # 배열에 들어있는 수의 개수
    q = deque(input()[1:-1].split(','))
    reverse = False
    error = False

    for p in P:
        if p == 'R': # 배열 뒤집기
            reverse = not reverse
        elif p == 'D': # 첫 번째 수 버리기
            if n > 0:
                if reverse is True: q.pop()
                else: q.popleft()
                n -= 1
            else: # 빈 배열에 D를 사용한 경우 에러 발생
                print("error")
                error = True
                break
            
    if error is False:
        if q:
            if reverse:
                q.reverse() 
            print('[' + ','.join(q) + ']')
        else:
            print('[]')