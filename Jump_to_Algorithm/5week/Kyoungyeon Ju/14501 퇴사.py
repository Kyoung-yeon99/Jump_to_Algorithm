N = int(input())
T, P = [], []
d = [0] * (N+1)

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

for i in range(N-1, -1, -1):  # 역방향으로
    if T[i] + i > N:  # 상담시작날과 상담 기간의 합이 퇴사일을 넘어가면
        d[i] = d[i+1]  # 뒤의 값 가져옴
    else:
        # T[i] + i 는 상담 시작 날과 상담 기간의 합, 즉 상담 완료날(새 상담 시작날)
        # 뒤의 값(상담X)와 상담완료날 d의 값(상담O) 중 큰값
        d[i] = max(d[i+1], d[T[i]+i] + P[i])
        #print("i=", i, "d[i+1]=", d[i+1], "d[i]=", d[i])
        #print("d[i+T[i]]", d[i+T[i]], "P[i]=", P[i])


print(d[0])

# 역방향 아이디어가 떠올리기 어려움



"""
for i in range(N):
    day -= 1
    print("i=", i, "day=", day)
    if day == 0:
        if T[i] == 1:
            day += 1
            result += P[i]
            print("T[i]==1일 때",)
        elif i == N-1:
            break
        else:
            day = T[i]
            result += P[i]
    else:
        continue
"""