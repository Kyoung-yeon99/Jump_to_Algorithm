# https://www.acmicpc.net/problem/1966

from collections import deque

test_case = int(input())  # test case 개수


def print_queue():
    n, index = map(int, input().split())  # 문서 개수, 큐에서 몇번째로 인쇄되는지 궁금한 인덱스

    cnt = 0  # 개수 세기
    q = deque(list(map(int, input().split())))  # 큐 생성

    while q:
        if q[0] == max(q):  # 우선순위가 가장 높을 경우
            cnt += 1
            if index == 0:  # 첫번째 인덱스의 경우.
                print(cnt)
                break
            else:  # 아니라면 큐에서 제거
                q.popleft()  # 앞에서 제거한다.
                index -= 1
        else:  # 우선순위가 가장 높지 않은 경우
            q.rotate(-1)  # 요소를 이동(왼쪽->오른쪽)
            index = (index - 1) % len(q)  # index-1을 해주는데, 모듈러 연산을 통해 음수가 나오지 않게끔.
    return cnt


for t in range(test_case):
    ans = print_queue()
