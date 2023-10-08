import math
t = int(input())
for _ in range(t):
    sum_gcd = 0
    l = list(map(int, input().split()))
    for i in range(1, l[0]+1):
        for j in range(i+1, l[0]+1):
            sum_gcd += math.gcd(l[i], l[j])
    print(sum_gcd)