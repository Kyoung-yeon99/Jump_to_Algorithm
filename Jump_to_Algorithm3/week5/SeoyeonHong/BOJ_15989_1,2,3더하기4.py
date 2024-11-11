f = [0, 1, 2, 3]

for _ in range(int(input())):
    n = int(input())
 
    for i in range(len(f), n+1):
        w = 0
        if i % 2 == 0 : # 2의 합으로 나타낼 수 있는지 확인
            w += 1
        for j in range(i//2): # 2와 3의 합 또는 3의 합으로 나타낼 수 있는지 확인
            if (i - 2 * j) % 3 == 0:
                w += 1
        
        f.append(f[i-1] + w) # 2와 3의 합으로 나타낼 수 있는 경우의 수
    
    print(f[n])