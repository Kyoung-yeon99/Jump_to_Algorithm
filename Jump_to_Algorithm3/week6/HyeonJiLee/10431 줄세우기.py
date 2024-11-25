from collections import deque

P = int(input())

for tc in range(1,P+1):
    A = deque(map(int, input().split()[1:]))
    length = len(A)
    id = 1
    answer = 0
    # 우선 아무나 한 명을 뽑아 줄의 맨 앞에 세운다.
    orders = deque()
    while True:
        if len(orders) == length:
            print(f'{tc} {answer}')
            break

        # 그리고 그 다음부터는 학생이 한 명씩 줄의 맨 뒤에 서면서 다음 과정을 거친다.
        student = A.popleft()
        orders.append(student)
        # 자기 앞에 자기보다 키가 큰 학생이 없다면 그냥 그 자리에 서고 차례가 끝난다.
        if max(max(orders),student) == student:
            id += 1
        # 자기 앞에 자기보다 키가 큰 학생이 한 명 이상 있다면 그중 가장 앞에 있는 학생(A)의 바로 앞에 선다. 이때, A부터 그 뒤의 모든 학생들은 공간을 만들기 위해 한 발씩 뒤로 물러서게 된다.
        else:
            student = orders.pop()
            #가장 앞에있는 학생 id 찾기
            tmp_id = 0
            while True:
                if orders[tmp_id] > student:
                    orders.insert(tmp_id, student)
                    answer += len(orders) - tmp_id - 1
                    break
                else:
                    tmp_id+=1


