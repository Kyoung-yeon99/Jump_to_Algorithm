# 저녁 조합만 구해서 계산하면 메모리 초과를 피할 수 있다
import sys
INT_MAX = sys.maxsize

n = int(input())
p = [
    list(map(int, input().split()))
    for _ in range(n)
]
evening = [
    False for _ in range(n)
]
ans = INT_MAX


# 아침과 저녁의 차이를 계산
def calc():
    moring_sum = sum([
        p[i][j]
        for i in range(n)
        for j in range(n)
        if not evening[i] and not evening[j]  # 저녁에 해당하지 않는다면
    ])

    evening_sum = sum([
        p[i][j]
        for i in range(n)
        for j in range(n)
        if evening[i] and evening[j]
    ])

    return abs(moring_sum - evening_sum)


def find_min(curr_idx, cnt):
    global ans

    if cnt == n // 2:
        ans = min(ans, calc())
        return

    if curr_idx == n:
        return

        # curr_idx 업무를 아침에 하는 경우
    find_min(curr_idx + 1, cnt)

    # curr_idx 업무를 밤에 하는 경우
    evening[curr_idx] = True  # append
    find_min(curr_idx + 1, cnt + 1)  # 재귀
    evening[curr_idx] = False  # pop


find_min(0, 0)

print(ans)


'''
# 메모리 초과
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

choice_list = [] # 각 항목의 절반은 아침, 절반은 저녁

# 0~total 수 중 num 개의 수를 뽑아서 ret_list에 저장하라
ret = []
def choice(num, ret_list, total):
    if len(ret) == num:
        ret_list.append(list(ret))
        return

    for i in range(total):
        if i not in ret:
            ret.append(i)
            choice(num, ret_list, total)
            ret.pop()

choice(n, choice_list, n)

def make_sum(cal_list, day):
    # call list 에 담긴 인덱스
    # 계산할 리스트를 받아서 더할 i, j를 뽑아내서 더함
    temp_sum = 0
    for c in cal_list:
        i = day[c[0]]
        j = day[c[1]]
        temp_sum += board[i][j]
    return temp_sum

diff = float('inf')

for ch in choice_list:
    idx_list = []
    morning = ch[:n//2]
    evening = ch[n//2:]

    # 각 항목당 2개씩 뽑아서 더해주기
    choice(2, idx_list, n//2)
    diff = min(diff, abs(make_sum(idx_list, morning) - make_sum(idx_list, evening)))

print(diff)

'''