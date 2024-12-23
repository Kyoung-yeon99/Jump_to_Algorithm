# 햄버거를 먹을 수 있는 사람의 최대 수
N, K = map(int, input().split())
info = list(input())
count = 0
for i in range(N):
    if info[i] == 'H': # 햄버거일 경우
        for j in range(i+1, min(i+K+1, N)): # 오른쪽에 가장 가까운 사람에게 준다
            if info[j] == 'P':
                info[i] = 'X'
                info[j] = 'X'
                count += 1
                break
    elif info[i] == 'P': # 사람일 경우
        for j in range(i+1, min(i+K+1, N)): # 오른쪽에 가까운 햄버거를 먹는다
            if info[j] == 'H':
                info[i] = 'X'
                info[j] = 'X'
                count += 1
                break

print(count)
