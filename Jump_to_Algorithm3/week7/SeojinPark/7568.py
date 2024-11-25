n=int(input())
lst=[]

for i in range(n):
    w,h=map(int,input().split())
    lst.append((w, h))  # 튜플로 저장 (더 안전함)

for i in lst:
    rank = 1
    for j in lst:
        if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    print(rank, end = " ")
