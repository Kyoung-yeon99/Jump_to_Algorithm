'''
- 아스키코드 순서에 따라 백 트래킹을 수행한다.

- 백 트래킹을 통해 모든 수식을 만들었다면 수식 사이사이에 숫자를 넣어 본다.

- 수식과 숫자를 합쳤다면 eval를 통해 수식이 0이 되는지 확인한다.

- 공백이 있을 수 있으므로 replace를 통해 공백을 제거한다.

- 아스키코드 순서에 따라 백 트래킹 했기 때문에 결과를 바로 출력하면 된다.
https://fre2-dom.tistory.com/463
'''

import sys
import copy


# 아스키 코드 순서에 따라 백 트래킹
def back_tracking(v):
    # 수식 개수가 n -1 개면 수식을 arr에 추가
    if len(v) == n - 1:
        arr.append(copy.deepcopy(v))
        return

    # 아스키 코드 34
    v.append(' ')
    back_tracking(v)
    v.pop()

    # 아스키 코드 44
    v.append('+')
    back_tracking(v)
    v.pop()

    # 아스키 코드 45
    v.append('-')
    back_tracking(v)
    v.pop()


t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    arr = []
    back_tracking([])

    # 모든 수식을 확인
    for i in arr:
        temp = ""
        # 수식을 숫자 사이 사이에 추가
        for j in range(1, n):
            temp += str(j) + str(i[j - 1])
        temp += str(n)

        # eval를 통해 수식을 더한 수가 0 인지 비교
        # replace는 공백을 제거
        if eval(temp.replace(' ', '')) == 0:
            print(temp)

    print()
