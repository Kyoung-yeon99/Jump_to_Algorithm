# 줄을 어떻게 서야 하는지 출력
N = int(input()) # 사람의 수
order = list(map(int, input().split())) # 자기보다 왼쪽에 있고 키가 큰 사람의 수
people = [i for i in range(1, N+1)]
line = [N]
for i in range(N-2, -1, -1): # N-2번째 수부터 0번째 수까지
    line.insert(order[i], i+1) # 현재 줄 서 있는 사람들 중에서 order[i]번째에 서기
    
print(*line)
