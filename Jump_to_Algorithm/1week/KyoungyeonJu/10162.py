# 전자레인지
T = int(input())

if (str(T)[-1]) != '0':   # 다른 방법: T % 10 != 0
    print(-1)
else:
    a = T // 300
    T = T % 300
    b = T // 60
    T = T % 60
    c = T // 10
    print(a, b, c)
