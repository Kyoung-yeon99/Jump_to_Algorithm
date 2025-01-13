N = int(input())
current = input()
target = input()

#첫 번째 스위치를 누른 경우와 누르지 않은 경우...를 나누어 비교...

def onoff(arr, i):
    return '1' if arr[i] == '0' else '0'

def swtich(state, count):
    for i in range(1, N):
        #두번째 스위치부터 탐색
        if state[i-1] != target[i-1]:
            count += 1
            #스위치 켜고끄기(i-1, i)
            state = state[:i-1] + onoff(state, i-1) + onoff(state, i) + state[i+1:]
            #맨 마지막 스위치가 아닌 경우 i+1번째도 바꾸기
            if i < N-1:
                state = state[:i+1] + onoff(state, i+1) + state[i+2:]
    return count if state == target else 100001 #누를 수 있는 최대 횟수 + 1

# 첫 번째 스위치를 누르지 않은 경우
result1 = swtich(current, 0)

# 첫 번째 스위치를 누른 경우
flipped = onoff(current, 0) + onoff(current, 1) + current[2:]
result2 = swtich(flipped, 1)

min_switches = min(result1, result2)
min_switches = min_switches if min_switches != 100001 else -1

print(min_switches)