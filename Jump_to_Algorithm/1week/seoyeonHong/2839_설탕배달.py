n = int(input())
a = 0
t = n

if n // 5 >= 1:
    a = n // 5
    t = n - a * 5
    if t == 0:
        print(a)
    elif t % 3 == 0:
        print(a + (t // 3))
    else:
        while(a > 0):
            a -= 1
            t = n - a * 5
            if t % 3 == 0:
                print(a + (t // 3))
                break
        if a == 0 and ((t % 3) != 0):
            print(-1)
elif n == 3:
    print(1)
else: 
    print(-1)
